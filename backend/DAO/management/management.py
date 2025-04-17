from pymongo import MongoClient
from user_dao import UserDAO
from post_dao import PostDAO
from comment_dao import CommentDAO
from image_dao import ImageDAO
from video_dao import VideoDAO

class Management:
    def __init__(self, db_url="mongodb+srv://nhiensu1306:nhiensu0905@blackwolf.pgsd6m8.mongodb.net/", db_name="BlackWolf"):
        self.client = MongoClient(db_url)
        self.db = self.client[db_name]
        
        # Initialize DAOs with the shared database connection
        self.user = UserDAO(self.db)
        self.post = PostDAO(self.db)
        self.comment = CommentDAO(self.db)
        self.image = ImageDAO(self.db)
        self.video = VideoDAO(self.db)

    def __del__(self):
        # Close the database connection when the Management object is destroyed
        self.client.close()

    def getUser(self, userID: str):
        return self.user.get(userID)

    def createUser(self, data: dict):
        user_obj = self.user.model_class(**data)
        self.user.add(user_obj)

    def deleteUser(self, userID: str):
        self.user.delete(userID)

    def getPost(self, postID: str):
        return self.post.get(postID)

    def createPost(self, data: dict):
        post_obj = self.post.model_class(**data)
        self.post.add(post_obj)

    def getComments(self, postID: str):
        return self.comment.getByPost(postID)

    def addComment(self, data: dict):
        comment_obj = self.comment.model_class(**data)
        self.comment.add(comment_obj)

    def getImages(self, postID: str):
        return self.image.getByPost(postID)

    def uploadImage(self, data: dict):
        image_obj = self.image.model_class(**data)
        self.image.add(image_obj)

    def getVideos(self, postID: str):
        return self.video.getByPost(postID)

    def uploadVideo(self, data: dict):
        video_obj = self.video.model_class(**data)
        self.video.add(video_obj)
