from datetime import datetime
import json

class Video:
    def __init__(self, user_id: str, post_id: str, url: str, duration: float, uploaded_at: datetime = None):
        self.video_id = None  # Will be auto-set by MongoDB
        self.user_id = user_id
        self.post_id = post_id
        self.url = url
        self.duration = duration
        self.uploaded_at = uploaded_at or datetime.utcnow()

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
            return True
        except Exception:
            return False

# comment id,..