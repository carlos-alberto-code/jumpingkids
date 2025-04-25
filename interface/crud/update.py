from abc import ABC, abstractmethod
from typing import TypeVar, Generic


T = TypeVar('T')


class UpdateEntity(ABC, Generic[T]):
    @abstractmethod
    def update(self, entity: T): pass


class UpdateManyEntities(ABC, Generic[T]):
    @abstractmethod
    def update_many(self, entities: list[T]): pass
    