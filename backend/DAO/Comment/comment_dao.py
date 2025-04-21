from typing import List, Optional
from bson.objectid import ObjectId
from comment import Comment
from dao_interface import ICommentDAO
import logging

class DatabaseError(Exception):
    pass

class CommentDAO(ICommentDAO):
    def __init__(self, db):
        self.db = db
        self.collection = self.db["comments"]
        self.logger = logging.getLogger(__name__)

    def getAll(self) -> List[Comment]:
        try:
            comments = self.collection.find()
            return [Comment(**c) for c in comments]
        except Exception as e:
            self.logger.error(f"Error getting all comments: {str(e)}")
            raise DatabaseError(f"Error getting all comments: {str(e)}")

    def get(self, comment_id: str) -> Optional[Comment]:
        try:
            comment = self.collection.find_one({"_id": ObjectId(comment_id)})
            return Comment(**comment) if comment else None
        except Exception as e:
            self.logger.error(f"Error getting comment {comment_id}: {str(e)}")
            raise DatabaseError(f"Error getting comment {comment_id}: {str(e)}")

    def getByPost(self, post_id: str) -> List[Comment]:
        try:
            comments = self.collection.find({"post_id": post_id})
            return [Comment(**c) for c in comments]
        except Exception as e:
            self.logger.error(f"Error getting comments for post {post_id}: {str(e)}")
            raise DatabaseError(f"Error getting comments for post {post_id}: {str(e)}")

    def add(self, comment: Comment) -> bool:
        try:
            if not comment.is_valid():
                self.logger.warning("Attempted to add invalid comment")
                return False
                
            result = self.collection.insert_one(comment.__dict__)
            return bool(result.inserted_id)
        except Exception as e:
            self.logger.error(f"Error adding comment: {str(e)}")
            raise DatabaseError(f"Error adding comment: {str(e)}")

    def update(self, comment_id: str, updated_comment: Comment) -> bool:
        try:
            if not updated_comment.is_valid():
                self.logger.warning("Attempted to update comment with invalid data")
                return False
                
            result = self.collection.update_one(
                {"_id": ObjectId(comment_id)},
                {"$set": updated_comment.__dict__}
            )
            return result.modified_count > 0
        except Exception as e:
            self.logger.error(f"Error updating comment {comment_id}: {str(e)}")
            raise DatabaseError(f"Error updating comment {comment_id}: {str(e)}")

    def delete(self, comment_id: str) -> bool:
        try:
            result = self.collection.delete_one({"_id": ObjectId(comment_id)})
            return result.deleted_count > 0
        except Exception as e:
            self.logger.error(f"Error deleting comment {comment_id}: {str(e)}")
            raise DatabaseError(f"Error deleting comment {comment_id}: {str(e)}")

    def like(self, comment_id: str, user_id: str) -> bool:
        try:
            # Prevent multiple likes from same user
            result = self.collection.update_one(
                {
                    "_id": ObjectId(comment_id),
                    "liked_by": {"$ne": user_id}
                },
                {
                    "$inc": {"like_count": 1},
                    "$addToSet": {"liked_by": user_id}
                }
            )
            return result.modified_count > 0
        except Exception as e:
            self.logger.error(f"Error liking comment {comment_id} by user {user_id}: {str(e)}")
            raise DatabaseError(f"Error liking comment {comment_id} by user {user_id}: {str(e)}")
