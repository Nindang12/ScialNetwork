from abc import ABC, abstractmethod
from typing import List, Optional
from post import Post

class IPostDAO(ABC):
    @abstractmethod
    def getAll(self) -> List[Post]:
        """Retrieve all posts from the database."""
        pass

    @abstractmethod
    def get(self, post_id: str) -> Optional[Post]:
        """Retrieve a post by its ID."""
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
