from datetime import datetime
import json
import logging
from post_interface import IPost

class Post(IPost):
    def __init__(self, user_id: str, video_id: list, image_id: list, content: str, createdAt: datetime = None):
        """Initialize a new Post instance.
        
        Args:
            userID (str): ID of the user who created the post
            video_id (list): List of video IDs attached to the post
            image_id (list): List of image IDs attached to the post
            content (str): Text content of the post
            createdAt (datetime, optional): Creation timestamp. Defaults to current time.
        """
        self.post_id = None  # Will be set by MongoDB
        self.user_id = user_id
        self.video_id = video_id
        self.image_id = image_id
        self.content = content
        self.createdAt = createdAt or datetime.utcnow()

    def to_json(self) -> str:
        """Convert the post to JSON string.
        
        Returns:
            str: JSON representation of the post
        """
        return json.dumps(self.__dict__, default=str)

    def create(self, data: dict) -> bool:
        """Create a post from dictionary data.
        
        Args:
            data (dict): Dictionary containing post data
            
        Returns:
            bool: True if creation was successful, False otherwise
        """
        try:
            self.post_id = data.get("post_id")
            self.user_id = data.get("user_id")
            self.video_id = data.get("video_id", [])
            self.image_id = data.get("image_id", [])
            self.content = data.get("content")
            self.createdAt = data.get("createdAt", datetime.utcnow())
            return True
        except Exception as e:
            logging.error(f"Error creating post: {str(e)}")
            return False
