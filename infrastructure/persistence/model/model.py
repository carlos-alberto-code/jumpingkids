from sqlalchemy import Integer, String, ForeignKey, Column, Table
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


class SubscriptionEntity(Base):
    """
    Representa una suscripción a un servicio. Cada suscripción tiene un nombre, una fecha de inicio y una fecha de finalización. La fecha de finalización se calcula automáticamente al agregar 30 días a la fecha de inicio.
    """
    __tablename__ = "subscriptions"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(30), nullable=False, unique=True)


class CategoryEntity(Base):
    """
    Representa una categoría de rutina. Ejemplos de categorías de rutina incluyen Yoga, Spinning, Crossfit, Fuerza, Resistencia, etc. Cada categoría puede tener múltiples rutinas asociadas.
    """
    __tablename__ = "categories"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False, unique=True)

    routines: Mapped[list["RoutineEntity"]] = relationship("RoutineEntity", secondary="categories_routines", back_populates="categories", lazy="selectin")

    def __repr__(self):
        return f"CategoryEntity(id={self.id}, name={self.name})"


class RoutineEntity(Base):
    """
    Representa una rutina de ejercicio. Cada rutina puede tener un nombre, una descripción y una categoría asociada. Las rutinas pueden estar asociadas con múltiples ejercicios.
    """
    __tablename__ = "routines"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False, unique=True)
    description: Mapped[str] = mapped_column(String(255), nullable=False)

    categories: Mapped[list["CategoryEntity"]] = relationship("CategoryEntity", secondary="categories_routines", back_populates="routines", lazy="selectin")
    exercises: Mapped[list["ExerciseEntity"]] = relationship("ExerciseEntity", secondary="routines_exercises", lazy="selectin")

    def __repr__(self):
        return f"RoutineEntity(id={self.id}, name={self.name})"


CategoryRoutineEntity = Table(
    "categories_routines",
    Base.metadata,
    Column("category_id", Integer, ForeignKey("categories.id"), primary_key=True),
    Column("routine_id", Integer, ForeignKey("routines.id"), primary_key=True),
)


class ExerciseEntity(Base):
    """
    Representa un ejercicio individual. Cada ejercicio puede tener un nombre y una descripción. Los ejercicios pueden estar asociados con múltiples rutinas.
    """
    __tablename__ = "exercises"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    description: Mapped[str] = mapped_column(String(255), nullable=False)

    def __repr__(self):
        return f"ExerciseEntity(id={self.id}, name={self.name})"


RoutineExerciseEntity = Table(
    "routines_exercises",
    Base.metadata,
    Column("routine_id", Integer, ForeignKey("routines.id"), primary_key=True),
    Column("exercise_id", Integer, ForeignKey("exercises.id"), primary_key=True),
)

class TutorEntity(Base):
    """
    Representa un tutor o cuidador de un niño. Cada tutor puede tener un nombre completo y puede estar asociado con múltiples niños.
    """
    __tablename__ = "tutors"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    full_name: Mapped[str] = mapped_column(String(100), nullable=False)
    username: Mapped[str] = mapped_column(String(50), nullable=False, unique=True)
    password: Mapped[str] = mapped_column(String(255), nullable=False)
    subscription_type_id: Mapped[int] = mapped_column(Integer, ForeignKey("subscriptions.id"), nullable=False)
    subscription: Mapped["SubscriptionEntity"] = relationship("SubscriptionEntity", lazy="selectin")

    children: Mapped[list["ChildEntity"]] = relationship("ChildEntity", back_populates="tutor", lazy="selectin")

    def __repr__(self):
        return f"TutorEntity(id={self.id}, full_name={self.full_name})"


class ChildEntity(Base):
    """
    Representa a un niño que realiza las rutinas. Cada niño puede tener un nombre completo, una edad y un tutor asociado. Los niños pueden estar asociados con múltiples rutinas a través de la tabla de asignación.
    """
    __tablename__ = "children"
    

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    full_name: Mapped[str] = mapped_column(String(100), nullable=False)
    tutor_id: Mapped[int] = mapped_column(Integer, ForeignKey("tutors.id"), nullable=False)
    username: Mapped[str] = mapped_column(String(50), nullable=False, unique=True)
    password: Mapped[str] = mapped_column(String(255), nullable=False)
    subscription_type: Mapped[SubscriptionTypeEnum] = mapped_column(Enum(SubscriptionTypeEnum), nullable=False, default=SubscriptionTypeEnum.FREE)

    tutor: Mapped["TutorEntity"] = relationship("TutorEntity", back_populates="children", lazy="selectin")
    favorite_routines: Mapped[list["RoutineEntity"]] = relationship("RoutineEntity", secondary="favorite_routines",lazy="selectin")

    def __repr__(self):
        return f"ChildEntity(id={self.id}, full_name={self.full_name})"


FavoriteRoutinesEntity = Table(
    "favorite_routines",
    Base.metadata,
    Column("child_id", Integer, ForeignKey("children.id"), primary_key=True, nullable=False),
    Column("routine_id", Integer, ForeignKey("routines.id"), primary_key=True, nullable=False),
)