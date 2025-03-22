from typing import Type, TypeVar, Generic

from sqlalchemy.orm import Session

from infrastructure.persistence.model.model import Base


T = TypeVar("T", bound=Base)


class Repository(Generic[T]):

    def __init__(self, model: Type[T], session: Session):
        self._model = model
        self._session = session

    def get_by_id(self, id: int) -> T | None:
        return self._session.get(self._model, id)

    def add(self, entity: T) -> None:
        self._session.add(entity)
        self._session.commit()

    def update(self, entity: T) -> None:
        self._session.merge(entity)
        self._session.commit()

    def delete(self, entity: T) -> None:
        self._session.delete(entity)
        self._session.commit()
