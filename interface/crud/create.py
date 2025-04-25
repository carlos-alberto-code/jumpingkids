from abc import ABC, abstractmethod
from typing import TypeVar, Generic


T = TypeVar('T')


class CreateEntity(ABC, Generic[T]):

    @abstractmethod
    def create(self, entity: T) -> T: pass


class CreateManyEntities(ABC, Generic[T]):

    @abstractmethod
    def create_many(self, entities: list[T]) -> list[T]: pass
