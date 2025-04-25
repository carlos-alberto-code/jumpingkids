from abc import ABC, abstractmethod
from typing import TypeVar, Generic


T = TypeVar('T')


class CreateEntity(ABC, Generic[T]):

    @abstractmethod
    def create(self, domain_object: T): pass


class CreateManyEntities(ABC, Generic[T]):

    @abstractmethod
    def create_many(self, domain_objects: list[T]): pass
