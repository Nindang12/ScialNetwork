from typing import List, Optional
from bson.objectid import ObjectId
from video import Video
from dao_interface import IVideoDAO
import logging

class DatabaseError(Exception):
    pass

class VideoDAO(IVideoDAO):
    def __init__(self, db):
        self.db = db
        self.collection = self.db["videos"]
        self.logger = logging.getLogger(__name__)

    def getAll(self) -> List[Video]:
        try:
            videos = self.collection.find()
            return [Video(**v) for v in videos]
        except Exception as e:
            self.logger.error(f"Error getting all videos: {str(e)}")
            raise DatabaseError(f"Error getting all videos: {str(e)}")

    def get(self, video_id: str) -> Optional[Video]:
        try:
            video = self.collection.find_one({"_id": ObjectId(video_id)})
            return Video(**video) if video else None
        except Exception as e:
            self.logger.error(f"Error getting video {video_id}: {str(e)}")
            raise DatabaseError(f"Error getting video {video_id}: {str(e)}")

    def getByPost(self, post_id: str) -> List[Video]:
        try:
            videos = self.collection.find({"post_id": post_id})
            return [Video(**v) for v in videos]
        except Exception as e:
            self.logger.error(f"Error getting videos for post {post_id}: {str(e)}")
            raise DatabaseError(f"Error getting videos for post {post_id}: {str(e)}")

    def add(self, video: Video) -> bool:
        try:
            if not video.is_valid():
                self.logger.warning("Attempted to add invalid video")
                return False
                
            result = self.collection.insert_one(video.__dict__)
            return bool(result.inserted_id)
        except Exception as e:
            self.logger.error(f"Error adding video: {str(e)}")
            raise DatabaseError(f"Error adding video: {str(e)}")

    def update(self, video_id: str, updated_video: Video) -> bool:
        try:
            if not updated_video.is_valid():
                self.logger.warning("Attempted to update video with invalid data")
                return False
                
            result = self.collection.update_one(
                {"_id": ObjectId(video_id)},
                {"$set": updated_video.__dict__}
            )
            return result.modified_count > 0
        except Exception as e:
            self.logger.error(f"Error updating video {video_id}: {str(e)}")
            raise DatabaseError(f"Error updating video {video_id}: {str(e)}")

    def delete(self, video_id: str) -> bool:
        try:
            result = self.collection.delete_one({"_id": ObjectId(video_id)})
            return result.deleted_count > 0
        except Exception as e:
            self.logger.error(f"Error deleting video {video_id}: {str(e)}")
            raise DatabaseError(f"Error deleting video {video_id}: {str(e)}")
