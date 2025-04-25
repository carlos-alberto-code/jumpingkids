from abc import ABC, abstractmethod
from typing import Generic, TypeVar


T = TypeVar('T')

class GetById(ABC, Generic[T]):
    @abstractmethod
    def get_by_id(self, id: str) -> T: pass


class GetByName(ABC, Generic[T]):
    @abstractmethod
    def get_by_name(self, name: str) -> T: pass


class GetAll(ABC, Generic[T]):
    @abstractmethod
    def get_all(self) -> list[T]: pass
