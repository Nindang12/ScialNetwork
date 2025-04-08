from abc import ABC, abstractmethod
from image import Image

class IImageDAO(ABC):
    @abstractmethod
    def getAll(self) -> list:
        pass

    @abstractmethod
    def get(self, image_id: str) -> Image:
        pass

    @abstractmethod
    def getByPost(self, post_id: str) -> list:
        pass

    @abstractmethod
    def add(self, image: Image) -> bool:
        pass

    @abstractmethod
    def update(self, image_id: str, updated_image: Image) -> bool:
        pass
