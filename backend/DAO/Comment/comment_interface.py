from abc import ABC, abstractmethod

class IComment(ABC):
    @abstractmethod
    def to_json(self) -> str:
        pass

    @abstractmethod
    def create(self, data: dict) -> bool:
        pass
