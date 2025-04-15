from typing import TypeVar, Generic, Type, Any
from abc import ABC, abstractmethod
from domain.model import Child, Tutor, User, SubscriptionType
from infrastructure.persistence.model import ChildEntity, TutorEntity, Base

T = TypeVar('T', bound=User)
E = TypeVar('E', bound=Base)  # Entidad de base de datos

class BaseMapper(Generic[T, E], ABC):
    """
    Mapeador base abstracto para convertir entidades a modelos de dominio y viceversa.
    """
    def __init__(self, domain_class: Type[T]):
        self.domain_class = domain_class
    
    @abstractmethod
    def domain_to_entity(self, domain_obj: T) -> E:
        """Convierte un objeto de dominio a una entidad de base de datos"""
        pass
    
    @abstractmethod
    def entity_to_domain(self, entity_obj: E) -> T:
        """Convierte una entidad de base de datos a un objeto de dominio"""
        pass


class SubscriptionTypeMapper:
    """
    Clase utilitaria para mapear tipos de suscripción entre dominio y persistencia
    """
    @staticmethod
    def to_domain(db_type: SubscriptionTypeEnum) -> SubscriptionType:
        """Mapea el tipo de suscripción de la BD al dominio"""
        if db_type == SubscriptionTypeEnum.FREE:
            return SubscriptionType.FREE
        elif db_type == SubscriptionTypeEnum.PREMIUM:
            return SubscriptionType.PREMIUM
        else:
            return SubscriptionType.FREE
    
    @staticmethod
    def to_entity(domain_type: SubscriptionType) -> SubscriptionTypeEnum:
        """Mapea el tipo de suscripción del dominio a la BD"""
        if domain_type == SubscriptionType.FREE:
            return SubscriptionTypeEnum.FREE
        elif domain_type == SubscriptionType.PREMIUM:
            return SubscriptionTypeEnum.PREMIUM
        else:
            return SubscriptionTypeEnum.FREE


class ChildMapper(BaseMapper[Child, ChildEntity]):
    """
    Mapeador específico para la entidad Child
    """
    def __init__(self):
        super().__init__(Child)
    
    def domain_to_entity(self, domain_obj: Child) -> ChildEntity:
        """Convierte un objeto de dominio Child a una entidad ChildEntity"""
        entity = ChildEntity(
            id=domain_obj.id,
            full_name=domain_obj.full_name,
            username=domain_obj.username,
            password=domain_obj.password,
            subscription_type=SubscriptionTypeMapper.to_entity(domain_obj.suscription),
            tutor_id=domain_obj.tutor.id if domain_obj.tutor else None
        )
        return entity
    
    def entity_to_domain(self, entity_obj: ChildEntity) -> Child:
        """Convierte una entidad ChildEntity a un objeto de dominio Child"""
        # Para evitar recursión infinita, primero creamos el tutor sin los hijos
        tutor = Tutor(
            id=entity_obj.tutor.id,
            full_name=entity_obj.tutor.full_name,
            username=entity_obj.tutor.username,
            password=entity_obj.tutor.password,
            suscription=SubscriptionTypeMapper.to_domain(entity_obj.tutor.subscription_type),
            children=[]
        )
        
        # Luego creamos el niño con el tutor
        child = Child(
            id=entity_obj.id,
            full_name=entity_obj.full_name,
            username=entity_obj.username,
            password=entity_obj.password,
            suscription=SubscriptionTypeMapper.to_domain(entity_obj.subscription_type),
            tutor=tutor,
            favorite_routines=[]  # Aquí se podría añadir la lógica para mapear rutinas favoritas si es necesario
        )
        
        return child


class TutorMapper(BaseMapper[Tutor, TutorEntity]):
    """
    Mapeador específico para la entidad Tutor
    """
    def __init__(self):
        super().__init__(Tutor)
    
    def domain_to_entity(self, domain_obj: Tutor) -> TutorEntity:
        """Convierte un objeto de dominio Tutor a una entidad TutorEntity"""
        entity = TutorEntity(
            id=domain_obj.id,
            full_name=domain_obj.full_name,
            username=domain_obj.username,
            password=domain_obj.password,
            subscription_type=SubscriptionTypeMapper.to_entity(domain_obj.suscription)
        )
        return entity
    
    def entity_to_domain(self, entity_obj: TutorEntity) -> Tutor:
        """Convierte una entidad TutorEntity a un objeto de dominio Tutor"""
        # Crear una lista para almacenar los hijos mapeados
        children = []
        
        # Primero creamos el tutor sin los hijos
        tutor = Tutor(
            id=entity_obj.id,
            full_name=entity_obj.full_name,
            username=entity_obj.username,
            password=entity_obj.password,
            suscription=SubscriptionTypeMapper.to_domain(entity_obj.subscription_type),
            children=children
        )
        
        # Ahora mapeamos cada hijo y lo añadimos a la lista
        for child_entity in entity_obj.children:
            child = Child(
                id=child_entity.id,
                full_name=child_entity.full_name,
                username=child_entity.username,
                password=child_entity.password,
                suscription=SubscriptionTypeMapper.to_domain(child_entity.subscription_type),
                tutor=tutor,
                favorite_routines=[]
            )
            children.append(child)
        
        return tutor


class UserMapper:
    """
    Clase fachada para seleccionar el mapeador adecuado según el tipo de usuario
    """
    @staticmethod
    def get_mapper(domain_class: Type[User]) -> BaseMapper:
        if domain_class == Child:
            return ChildMapper()
        elif domain_class == Tutor:
            return TutorMapper()
        else:
            raise ValueError(f"Tipo no soportado: {domain_class}")
