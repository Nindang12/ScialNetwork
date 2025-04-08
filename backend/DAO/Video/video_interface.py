from abc import ABC, abstractmethod

class IVideo(ABC):
    @abstractmethod
    def to_json(self) -> str:
        pass

    @abstractmethod
    def create(self, data: dict) -> bool:
        pass
