from datetime import datetime
import json

class Image:
    def __init__(self, userID: str, postID: str, url: str, uploadedAt: datetime = None):
        self.image_id = None  # This will be set when inserted into MongoDB
        self.user_id = userID
        self.post_id = postID
        self.url = url
        self.uploaded_at = uploadedAt or datetime.utcnow()

    def to_json(self) -> str:
        return json.dumps(self.__dict__, default=str)

    def create(self, data: dict) -> bool:
        try:
            self.image_id = data.get("image_id")
            self.user_id = data.get("user_id")
            self.post_id = data.get("post_id")
            self.url = data.get("url")
            self.uploaded_at = data.get("uploaded_at", datetime.utcnow())
            return True
        except Exception:
            return False

# Comment id,