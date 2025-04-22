from abc import ABC, abstractmethod
from typing import List, Optional
from image import Image

class IImageDAO(ABC):
    @abstractmethod
    def getAll(self) -> List[Image]:
        pass

    @abstractmethod
    def get(self, image_id: str) -> Optional[Image]:
        pass

    @abstractmethod
    def getByPost(self, post_id: str) -> List[Image]:
        pass

    @abstractmethod
    def add(self, image: Image) -> bool:
        pass

    @abstractmethod
    def update(self, image_id: str, updated_image: Image) -> bool:
        pass

    @abstractmethod
    def delete(self, image_id: str) -> bool:
        pass

    @abstractmethod
    def getByUser(self, user_id: str) -> List[Image]:
        pass
