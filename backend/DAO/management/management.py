from typing import Dict, List, Optional
from DAO.User import User, UserDAO
from DAO.Post import Post, PostDAO
from DAO.Comment import Comment, CommentDAO
from DAO.Image import Image, ImageDAO
from DAO.Video import Video, VideoDAO
from DAO.management.ManagementInterface import ManagementInterface
from config import MONGODB_URL, MONGODB_DB_NAME
from pymongo import MongoClient
import logging

class Management(ManagementInterface):
    """Implementation of ManagementInterface for managing all entities."""
    
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.db = self._get_db()
        self.daos = self._get_daos()

    @staticmethod
    def _get_db():
        """Get MongoDB database connection."""
        try:
            client = MongoClient(MONGODB_URL)
            return client[MONGODB_DB_NAME]
        except Exception as e:
            logging.error(f"Error connecting to database: {str(e)}")
            raise

    def _get_daos(self) -> Dict:
        """Get all DAO instances."""
        return {
            'user': UserDAO(self.db),
            'post': PostDAO(self.db),
            'comment': CommentDAO(self.db),
            'image': ImageDAO(self.db),
            'video': VideoDAO(self.db)
        }

    def getAllUsers(self) -> List[User]:
        """Get all users in the system."""
        try:
            return self.daos['user'].getAll()
        except Exception as e:
            self.logger.error(f"Error getting all users: {str(e)}")
            raise

    def getUser(self, user_id: str) -> Optional[User]:
        """Get a user by ID."""
        try:
            return self.daos['user'].get(user_id)
        except Exception as e:
            self.logger.error(f"Error getting user {user_id}: {str(e)}")
            raise

    def findUserByEmail(self, email: str) -> Optional[User]:
        """Find a user by email."""
        try:
            return self.daos['user'].findByEmail(email)
        except Exception as e:
            self.logger.error(f"Error finding user by email {email}: {str(e)}")
            raise

    def createUser(self, data: dict) -> bool:
        """Create a new user."""
        try:
            if not data.get('email') or not data.get('password'):
                raise ValueError("Email and password are required")
            user_obj = self.daos['user'].model_class(**data)
            return self.daos['user'].add(user_obj)
        except Exception as e:
            self.logger.error(f"Error creating user: {str(e)}")
            raise

    def updateUser(self, user_id: str, data: dict) -> bool:
        """Update an existing user."""
        try:
            user_obj = self.daos['user'].model_class(**data)
            return self.daos['user'].update(user_id, user_obj)
        except Exception as e:
            self.logger.error(f"Error updating user {user_id}: {str(e)}")
            raise

    def deleteUser(self, user_id: str) -> bool:
        """Delete a user."""
        try:
            return self.daos['user'].delete(user_id)
        except Exception as e:
            self.logger.error(f"Error deleting user {user_id}: {str(e)}")
            raise

    # Post functions
    @staticmethod
    def get_all_posts():
        daos = Management._get_daos()
        return daos['post'].getAll()

    @staticmethod
    def get_post(post_id: str):
        daos = Management._get_daos()
        return daos['post'].get(post_id)

    @staticmethod
    def create_post(data: dict):
        daos = Management._get_daos()
        post_obj = daos['post'].model_class(**data)
        daos['post'].add(post_obj)

    @staticmethod
    def update_post(post_id: str, data: dict):
        daos = Management._get_daos()
        post_obj = daos['post'].model_class(**data)
        return daos['post'].update(post_id, post_obj)

    @staticmethod
    def delete_post(post_id: str):
        daos = Management._get_daos()
        return daos['post'].delete(post_id)

    @staticmethod
    def like_post(post_id: str, user_id: str):
        daos = Management._get_daos()
        return daos['post'].like(post_id, user_id)

    @staticmethod
    def repost_post(post_id: str, user_id: str):
        daos = Management._get_daos()
        return daos['post'].repost(post_id, user_id)

    # Comment functions
    @staticmethod
    def get_all_comments():
        daos = Management._get_daos()
        return daos['comment'].getAll()

    @staticmethod
    def get_comment(commentID: str):
        daos = Management._get_daos()
        return daos['comment'].get(commentID)

    @staticmethod
    def get_comments_by_post(post_id: str):
        daos = Management._get_daos()
        return daos['comment'].getByPost(post_id)

    @staticmethod
    def add_comment(data: dict):
        daos = Management._get_daos()
        comment_obj = daos['comment'].model_class(**data)
        daos['comment'].add(comment_obj)

    @staticmethod
    def update_comment(commentID: str, data: dict):
        daos = Management._get_daos()
        comment_obj = daos['comment'].model_class(**data)
        return daos['comment'].update(commentID, comment_obj)

    @staticmethod
    def delete_comment(commentID: str):
        daos = Management._get_daos()
        return daos['comment'].delete(commentID)

    @staticmethod
    def like_comment(comment_id: str, user_id: str):
        daos = Management._get_daos()
        return daos['comment'].like(comment_id, user_id)

    # Image functions
    @staticmethod
    def get_all_images():
        daos = Management._get_daos()
        return daos['image'].getAll()

    @staticmethod
    def get_image(imageID: str):
        daos = Management._get_daos()
        return daos['image'].get(imageID)

    @staticmethod
    def get_images_by_post(post_id: str):
        daos = Management._get_daos()
        return daos['image'].getByPost(post_id)

    @staticmethod
    def upload_image(data: dict):
        daos = Management._get_daos()
        image_obj = daos['image'].model_class(**data)
        daos['image'].add(image_obj)

    @staticmethod
    def update_image(imageID: str, data: dict):
        daos = Management._get_daos()
        image_obj = daos['image'].model_class(**data)
        return daos['image'].update(imageID, image_obj)

    # Video functions
    @staticmethod
    def get_all_videos():
        daos = Management._get_daos()
        return daos['video'].getAll()

    @staticmethod
    def get_video(videoID: str):
        daos = Management._get_daos()
        return daos['video'].get(videoID)

    @staticmethod
    def get_videos_by_post(post_id: str):
        daos = Management._get_daos()
        return daos['video'].getByPost(post_id)

    @staticmethod
    def upload_video(data: dict):
        daos = Management._get_daos()
        video_obj = daos['video'].model_class(**data)
        daos['video'].add(video_obj)

    @staticmethod
    def update_video(videoID: str, data: dict):
        daos = Management._get_daos()
        video_obj = daos['video'].model_class(**data)
        return daos['video'].update(videoID, video_obj)

    @staticmethod
    def delete_video(videoID: str):
        daos = Management._get_daos()
        return daos['video'].delete(videoID)
