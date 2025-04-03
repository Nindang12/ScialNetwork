from datetime import datetime
from typing import Optional, Dict

class Video:
    def __init__(self, user_id: str, post_id: Optional[str], url: str, uploaded_at: datetime, comment_id: Optional[str] = None, video_id: Optional[str] = None):
        self.video_id = video_id
        self.user_id = user_id
        self.post_id = post_id
        self.url = url
        self.comment_id = comment_id
        self.uploaded_at = uploaded_at

    def to_json(self) -> Dict:
        return {
            "video_id": self.video_id,
            "user_id": self.user_id,
            "post_id": self.post_id,
            "comment_id": self.comment_id,
            "url": self.url,
            "uploaded_at": self.uploaded_at.isoformat()
        }

    @staticmethod
    def create(dict_data: Dict) -> 'Video':
        return Video(
            video_id=str(dict_data.get('_id')),
            user_id=dict_data['user_id'],
            post_id=dict_data['post_id'],
            url=dict_data['url'],
            comment_id=dict_data.get('comment_id'),
            uploaded_at=datetime.fromisoformat(dict_data['uploaded_at'])
        )
