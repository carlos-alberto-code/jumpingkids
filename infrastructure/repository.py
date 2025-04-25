from typing import Type, TypeVar, Generic
from sqlalchemy import ColumnElement, select, and_
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

from infrastructure.database.model import Base
from infrastructure.database.connection import get_session


T = TypeVar("T", bound=Base)


class Repository(Generic[T]):

    def __init__(self, model: Type[T]):
        super().__init__()
        self._model = model
    
    def get_by(self, *conditions: ColumnElement[bool]) -> T | None:
        with get_session() as session:
            try:
                stmt = select(self._model).where(and_(*conditions))
                result = session.execute(stmt)
                return result.scalar_one_or_none()
            except SQLAlchemyError as e:
                # Considera logging aquí
                raise SQLAlchemyError(f"Error al obtener entidad: {str(e)}")

    def get_by_id(self, id: int) -> T | None:
        try:
            with get_session() as session:
                return session.get(self._model, id)
        except SQLAlchemyError as e:
            # Considera logging aquí
            raise Exception(f"Error al obtener entidad por ID: {str(e)}")
    
    def get_all(self) -> list[T] | None:
        try:
            with get_session() as session:
                return session.query(self._model).all()
        except SQLAlchemyError as e:
            raise Exception(f"Error al obtener todas las entidades: {str(e)}")
    
    def add(self, entity: T) -> T:
        try:
            with get_session() as session:
                session.add(entity)
                session.commit()
                session.refresh(entity)
                return entity
        except IntegrityError as e:
            session.rollback()
            raise Exception(f"Error de integridad al añadir entidad: {str(e)}")
        except SQLAlchemyError as e:
            session.rollback()
            raise Exception(f"Error al añadir entidad: {str(e)}")

    def update(self, entity: T) -> T:
        try:
            with get_session() as session:
                merged = session.merge(entity)
                session.commit()
                session.refresh(merged)
                return merged
        except SQLAlchemyError as e:
            session.rollback()
            raise Exception(f"Error al actualizar entidad: {str(e)}")
    
    def delete(self, entity: T) -> None:
        try:
            with get_session() as session:
                session.delete(entity)
                session.commit()
        except SQLAlchemyError as e:
            session.rollback()
            raise Exception(f"Error al eliminar entidad: {str(e)}")
