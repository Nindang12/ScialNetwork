from datetime import datetime
import json

class Post:
    def __init__(self, userID: str, video_id: list, image_id: list, content: str, createdAt: datetime = None):
        self.postID = None  # Will be set by MongoDB
        self.userID = userID
        self.video_id = video_id
        self.image_id = image_id
        self.content = content
        self.createdAt = createdAt or datetime.utcnow()

    def to_json(self) -> str:
        return json.dumps(self.__dict__, default=str)

    def create(self, data: dict) -> bool:
        try:
            self.postID = data.get("postID")
            self.userID = data.get("userID")
            self.video_id = data.get("video_id", [])
            self.image_id = data.get("image_id", [])
            self.content = data.get("content")
            self.createdAt = data.get("createdAt", datetime.utcnow())
            return True
        except Exception:
            return False
