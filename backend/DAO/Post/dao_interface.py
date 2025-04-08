from abc import ABC, abstractmethod
from post import Post

class IPostDAO(ABC):
    @abstractmethod
    def getAll(self) -> list:
        pass

    @abstractmethod
    def get(self, post_id: str) -> Post:
        pass

    @abstractmethod
    def add(self, post: Post) -> bool:
        pass

    @abstractmethod
    def update(self, post_id: str, updated_post: Post) -> bool:
        pass

    @abstractmethod
    def delete(self, post_id: str) -> bool:
        pass

    @abstractmethod
    def like(self, post_id: str, user_id: str) -> bool:
        pass

    @abstractmethod
    def repost(self, post_id: str, user_id: str) -> bool:
        pass
