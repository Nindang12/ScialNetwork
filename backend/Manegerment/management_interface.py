from abc import ABC, abstractmethod
from typing import Dict, List
from user import User
from post import Post
from comment import Comment
from image import Image
from video import Video

class Management_interface(ABC):

    @abstractmethod
    def getUser(self, userID: str) -> User:
        pass

    @abstractmethod
    def createUser(self, data: Dict) -> None:
        pass

    @abstractmethod
    def deleteUser(self, userID: str) -> None:
        pass

    @abstractmethod
    def getPost(self, postID: str) -> Post:
        pass

    @abstractmethod
    def createPost(self, data: Dict) -> None:
        pass

    @abstractmethod
    def getComments(self, postID: str) -> List[Comment]:
        pass

    @abstractmethod
    def addComment(self, data: Dict) -> None:
        pass

    @abstractmethod
    def getImages(self, postID: str) -> List[Image]:
        pass

    @abstractmethod
    def uploadImage(self, data: Dict) -> None:
        pass

    @abstractmethod
    def getVideos(self, postID: str) -> List[Video]:
        pass

    @abstractmethod
    def uploadVideo(self, data: Dict) -> None:
        pass
