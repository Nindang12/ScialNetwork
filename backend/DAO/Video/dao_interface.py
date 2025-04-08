from abc import ABC, abstractmethod
from video import Video

class IVideoDAO(ABC):
    @abstractmethod
    def getAll(self) -> list:
        pass

    @abstractmethod
    def get(self, video_id: str) -> Video:
        pass

    @abstractmethod
    def getByPost(self, post_id: str) -> list:
        pass

    @abstractmethod
    def add(self, video: Video) -> bool:
        pass

    @abstractmethod
    def update(self, video_id: str, updated_video: Video) -> bool:
        pass

    @abstractmethod
    def delete(self, video_id: str) -> bool:
        pass
