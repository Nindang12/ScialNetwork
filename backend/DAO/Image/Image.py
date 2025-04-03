from datetime import datetime
from typing import List, Dict, Optional

class Image:
    def __init__(self, user_id: str, post_id: Optional[str], url: str, uploaded_at: datetime, comment_id: Optional[str] = None, image_id: Optional[str] = None):
        self.image_id = image_id
        self.user_id = user_id
        self.post_id = post_id
        self.comment_id = comment_id  # Nếu có comment_id thì là ảnh của comment, ngược lại là của post
        self.url = url
        self.uploaded_at = uploaded_at

    def to_json(self) -> Dict:
        """Convert Image object to JSON/dict format"""
        return {
            "image_id": self.image_id,
            "user_id": self.user_id,
            "post_id": self.post_id,
            "comment_id": self.comment_id,
            "url": self.url,
            "uploaded_at": self.uploaded_at.isoformat()
        }

    @staticmethod
    def create(dict_data: Dict) -> 'Image':
        """Create an Image object from dictionary data"""
        return Image(
            image_id=dict_data.get('_id'),
            user_id=dict_data['user_id'],
            post_id=dict_data.get('post_id'),
            comment_id=dict_data.get('comment_id'),
            url=dict_data['url'],
            uploaded_at=datetime.fromisoformat(dict_data['uploaded_at'])
        )
