from datetime import datetime
import json
import re
from image_interface import IImage
import logging

class Image(IImage):
    def __init__(self, userID: str, postID: str, url: str, uploadedAt: datetime = None):
        if not self._validate_url(url):
            raise ValueError("Invalid URL format")
            
        self.image_id = None
        self.user_id = userID
        self.post_id = postID
        self.url = url
        self.uploaded_at = uploadedAt or datetime.utcnow()

    def _validate_url(self, url: str) -> bool:
        pattern = r'^https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+'
        return bool(re.match(pattern, url))

    def is_valid(self) -> bool:
        return all([
            self.user_id,
            self.post_id,
            self._validate_url(self.url)
        ])

    def to_json(self) -> str:
        return json.dumps(self.__dict__, default=str)

    def create(self, data: dict) -> bool:
        try:
            self.image_id = data.get("image_id")
            self.user_id = data.get("user_id")
            self.post_id = data.get("post_id")
            self.url = data.get("url")
            self.uploaded_at = data.get("uploaded_at", datetime.utcnow())
            return self.is_valid()
        except Exception as e:
            logging.error(f"Error creating image: {str(e)}")
            return False

# Comment id,