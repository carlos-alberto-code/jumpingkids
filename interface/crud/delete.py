from abc import ABC, abstractmethod
from typing import TypeVar, Generic


T = TypeVar('T')


class DeleteEntity(ABC, Generic[T]):

    @abstractmethod
    def delete(self, domain_object: T) -> None: pass


class DeleteManyEntities(ABC, Generic[T]):
    @abstractmethod
    def delete_many(self, domain_objects: list[T]) -> None: pass


class DeleteById(ABC, Generic[T]):
    @abstractmethod
    def delete_by_id(self, domain_object_id: int) -> None: pass


class DeleteByName(ABC, Generic[T]):
    @abstractmethod
    def delete_by_name(self, domain_object_name: str) -> None: pass
    