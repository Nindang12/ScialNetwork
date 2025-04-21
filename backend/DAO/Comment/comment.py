from datetime import datetime
import json
from comment_interface import IComment
import logging

class Comment(IComment):
    def __init__(self, post_id: str, user_id: str, content: str, created_at: datetime = None):
        """Initialize a new Comment instance."""
        if not content:
            raise ValueError("Content cannot be empty")
            
        self.comment_id = None
        self.post_id = post_id
        self.user_id = user_id
        self.content = content
        self.created_at = created_at or datetime.utcnow()
        self.like_count = 0

    def is_valid(self) -> bool:
        """Check if the comment is valid."""
        return all([
            self.post_id,
            self.user_id,
            self.content,
            self.like_count >= 0
        ])

    def to_json(self) -> str:
        """Convert the comment to JSON string."""
        return json.dumps(self.__dict__, default=str)

    def create(self, data: dict) -> bool:
        """Create a comment from dictionary data."""
        try:
            self.comment_id = data.get("comment_id")
            self.post_id = data.get("post_id")
            self.user_id = data.get("user_id")
            self.content = data.get("content")
            self.created_at = data.get("created_at", datetime.utcnow())
            self.like_count = data.get("like_count", 0)
            return self.is_valid()
        except Exception as e:
            logging.error(f"Error creating comment: {str(e)}")
            return False
