from typing import List, Optional
from pymongo import MongoClient
from bson import ObjectId
from Video import Video

class VideoDAO:
    def __init__(self, db_url="mongodb://localhost:27017/", db_name="mydatabase"):
        self.client = MongoClient(db_url)
        self.db = self.client[db_name]
        self.collection = self.db["videos"]

    def get_all(self) -> List[Video]:
        videos = self.collection.find()
        return [Video.create(video) for video in videos]

    def get(self, video_id: str) -> Optional[Video]:
        video = self.collection.find_one({"_id": ObjectId(video_id)})
        return Video.create(video) if video else None

    def get_by_post(self, post_id: str) -> List[Video]:
        videos = self.collection.find({"post_id": post_id})
        return [Video.create(video) for video in videos]

    def get_by_comment(self, comment_id: str) -> List[Video]:
        videos = self.collection.find({"comment_id": comment_id})
        return [Video.create(video) for video in videos]

    def add(self, video: Video) -> bool:
        try:
            video_dict = video.to_json()
            del video_dict['video_id']  # MongoDB sẽ tự tạo _id
            result = self.collection.insert_one(video_dict)
            video.video_id = str(result.inserted_id)  
            return True
        except Exception as e:
            print(f"Error adding video: {e}")
            return False

    def update(self, video_id: str, updated_video: Video) -> bool:
        try:
            result = self.collection.update_one(
                {"_id": ObjectId(video_id)},
                {"$set": updated_video.to_json()}
            )
            return result.modified_count > 0
        except Exception as e:
            print(f"Error updating video: {e}")
            return False
