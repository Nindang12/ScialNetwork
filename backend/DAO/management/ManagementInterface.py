from abc import ABC, abstractmethod
from typing import Dict, List, Optional
from DAO.User import User
from DAO.Post import Post
from DAO.Comment import Comment
from DAO.Image import Image
from DAO.Video import Video

class ManagementInterface(ABC):
    """Interface for managing all entities in the system."""
    
    @abstractmethod
    def getAllUsers(self) -> List[User]:
        """Get all users in the system."""
        pass

    @abstractmethod
    def getUser(self, user_id: str) -> Optional[User]:
        """Get a user by ID."""
        pass

    @abstractmethod
    def createUser(self, data: Dict) -> bool:
        """Create a new user."""
        pass

    @abstractmethod
    def updateUser(self, user_id: str, data: Dict) -> bool:
        """Update an existing user."""
        pass

    @abstractmethod
    def deleteUser(self, user_id: str) -> bool:
        """Delete a user."""
        pass

    @abstractmethod
    def getPost(self, post_id: str) -> Post:
        pass

    @abstractmethod
    def createPost(self, data: Dict) -> None:
        pass

    @abstractmethod
    def getComments(self, post_id: str) -> List[Comment]:
        pass

    @abstractmethod
    def addComment(self, data: Dict) -> None:
        pass

    @abstractmethod
    def getImages(self, post_id: str) -> List[Image]:
        pass

    @abstractmethod
    def uploadImage(self, data: Dict) -> None:
        pass

    @abstractmethod
    def getVideos(self, post_id: str) -> List[Video]:
        pass

    @abstractmethod
    def uploadVideo(self, data: Dict) -> None:
        pass
