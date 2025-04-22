from datetime import datetime
import json
import re
from video_interface import IVideo
import logging

class Video(IVideo):
    def __init__(self, user_id: str, post_id: str, url: str, duration: float, uploaded_at: datetime = None):
        """Initialize a new Video instance."""
        if not self._validate_url(url):
            raise ValueError("Invalid URL format")
        if not self._validate_duration(duration):
            raise ValueError("Duration must be positive")
            
        self.video_id = None
        self.user_id = user_id
        self.post_id = post_id
        self.url = url
        self.duration = duration
        self.uploaded_at = uploaded_at or datetime.utcnow()

    def _validate_url(self, url: str) -> bool:
        pattern = r'^https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+'
        return bool(re.match(pattern, url))

    def _validate_duration(self, duration: float) -> bool:
        return duration > 0

    def is_valid(self) -> bool:
        return all([
            self.user_id,
            self.post_id,
            self._validate_url(self.url),
            self._validate_duration(self.duration)
        ])

    def to_json(self) -> str:
        return json.dumps(self.__dict__, default=str)

    def create(self, data: dict) -> bool:
        try:
            self.video_id = data.get("video_id")
            self.user_id = data.get("user_id")
            self.post_id = data.get("post_id")
            self.url = data.get("url")
            self.duration = data.get("duration", 0.0)
            self.uploaded_at = data.get("uploaded_at", datetime.utcnow())
            return self.is_valid()
        except Exception as e:
            logging.error(f"Error creating video: {str(e)}")
            return False

