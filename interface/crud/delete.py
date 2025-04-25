from abc import ABC, abstractmethod
from typing import TypeVar, Generic


T = TypeVar('T')


class DeleteEntity(ABC, Generic[T]):

    @abstractmethod
    def delete(self, entity: T) -> None: pass


class DeleteManyEntities(ABC, Generic[T]):
    @abstractmethod
    def delete_many(self, entities: list[T]) -> None: pass


class DeleteById(ABC, Generic[T]):
    @abstractmethod
    def delete_by_id(self, entity_id: str) -> None: pass


class DeleteByName(ABC, Generic[T]):
    @abstractmethod
    def delete_by_name(self, entity_name: str) -> None: pass
    