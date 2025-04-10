from abc import ABC, abstractmethod

class IUser(ABC):
    @abstractmethod
    def to_json(self) -> str:
        pass

    @abstractmethod
    def create(self, dict: dict) -> bool:
        pass
