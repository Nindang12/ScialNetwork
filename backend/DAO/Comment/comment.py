from datetime import datetime
import json

class Comment:
    def __init__(self, post_id: str, user_id: str, content: str, created_at: datetime = None):
        self.comment_id = None  # Will be auto-set by MongoDB
        self.post_id = post_id
        self.user_id = user_id
        self.content = content
        self.created_at = created_at or datetime.utcnow()
        self.like_count = 0

    def to_json(self) -> str:
        return json.dumps(self.__dict__, default=str)

    def create(self, data: dict) -> bool:
        try:
            self.comment_id = data.get("comment_id")
            self.post_id = data.get("post_id")
            self.user_id = data.get("user_id")
            self.content = data.get("content")
            self.created_at = data.get("created_at", datetime.utcnow())
            self.like_count = data.get("like_count", 0)
            return True
        except Exception:
            return False
