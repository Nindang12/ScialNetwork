from abc import ABC, abstractmethod
from comment import Comment

class ICommentDAO(ABC):
    @abstractmethod
    def getAll(self) -> list:
        pass

    @abstractmethod
    def get(self, comment_id: str) -> Comment:
        pass

    @abstractmethod
    def getByPost(self, post_id: str) -> list:
        pass

    @abstractmethod
    def add(self, comment: Comment) -> bool:
        pass

    @abstractmethod
    def update(self, comment_id: str, updated_comment: Comment) -> bool:
        pass

    @abstractmethod
    def delete(self, comment_id: str) -> bool:
        pass

    @abstractmethod
    def like(self, comment_id: str, user_id: str) -> bool:
        pass
