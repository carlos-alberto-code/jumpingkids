from abc import ABC, abstractmethod
from typing import Generic, TypeVar


T = TypeVar('T')

class GetById(ABC, Generic[T]):
    @abstractmethod
    def get_by_id(self, domain_object_id: int) -> T | None: pass


class GetByName(ABC, Generic[T]):
    @abstractmethod
    def get_by_name(self, domain_object_name: str) -> T | None: pass


class GetByUsername(ABC, Generic[T]):
    @abstractmethod
    def get_by_username(self, username: str) -> T | None: pass


class GetAll(ABC, Generic[T]):
    @abstractmethod
    def get_all(self) -> list[T] | None: pass
