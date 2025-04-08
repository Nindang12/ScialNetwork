from pymongo import MongoClient
from bson.objectid import ObjectId
from video import Video

class VideoDAO:
    def __init__(self, db_url="mongodb://localhost:27017/", db_name="postDB"):
        self.client = MongoClient(db_url)
        self.db = self.client[db_name]
        self.collection = self.db["videos"]

    def getAll(self) -> list:
        videos = self.collection.find()
        return [Video(**v) for v in videos]

    def get(self, video_id: str) -> Video:
        video = self.collection.find_one({"_id": ObjectId(video_id)})
        return Video(**video) if video else None

    def getByPost(self, post_id: str) -> list:
        videos = self.collection.find({"post_id": post_id})
        return [Video(**v) for v in videos]

    def add(self, video: Video) -> bool:
        result = self.collection.insert_one(video.__dict__)
        return bool(result.inserted_id)

    def update(self, video_id: str, updated_video: Video) -> bool:
        result = self.collection.update_one(
            {"_id": ObjectId(video_id)},
            {"$set": updated_video.__dict__}
        )
        return result.modified_count > 0

    def delete(self, video_id: str) -> bool:
        result = self.collection.delete_one({"_id": ObjectId(video_id)})
        return result.deleted_count > 0
