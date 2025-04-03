from datetime import datetime
from typing import List, Dict

class Post:
    def __init__(self, userID: str, content: str, mediaURLs: List[str], createdAt: datetime, postID: str = None):
        self.postID = postID
        self.userID = userID
        self.content = content
        self.mediaURLs = mediaURLs
        self.createdAt = createdAt

    def to_json(self) -> Dict:
        """Convert Post object to JSON/dict format"""
        return {
            "postID": self.postID,
            "userID": self.userID,
            "content": self.content,
            "mediaURLs": self.mediaURLs,
            "createdAt": self.createdAt.isoformat()
        }

    @staticmethod
    def create(dict_data: Dict) -> 'Post':
        """Create a Post object from dictionary data"""
        return Post(
            postID=dict_data.get('postID'),
            userID=dict_data['userID'],
            content=dict_data['content'],
            mediaURLs=dict_data.get('mediaURLs', []),
            createdAt=datetime.fromisoformat(dict_data['createdAt']) if isinstance(dict_data['createdAt'], str) else dict_data['createdAt']
        )
