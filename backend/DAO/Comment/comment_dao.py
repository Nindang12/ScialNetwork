from pymongo import MongoClient
from bson.objectid import ObjectId
from comment import Comment

class CommentDAO:
    def __init__(self, db_url="mongodb://localhost:27017/", db_name="postDB"):
        self.client = MongoClient(db_url)
        self.db = self.client[db_name]
        self.collection = self.db["comments"]

    def getAll(self) -> list:
        comments = self.collection.find()
        return [Comment(**c) for c in comments]

    def get(self, comment_id: str) -> Comment:
        comment = self.collection.find_one({"_id": ObjectId(comment_id)})
        return Comment(**comment) if comment else None

    def getByPost(self, post_id: str) -> list:
        comments = self.collection.find({"post_id": post_id})
        return [Comment(**c) for c in comments]

    def add(self, comment: Comment) -> bool:
        result = self.collection.insert_one(comment.__dict__)
        return bool(result.inserted_id)

    def update(self, comment_id: str, updated_comment: Comment) -> bool:
        result = self.collection.update_one(
            {"_id": ObjectId(comment_id)},
            {"$set": updated_comment.__dict__}
        )
        return result.modified_count > 0

    def delete(self, comment_id: str) -> bool:
        result = self.collection.delete_one({"_id": ObjectId(comment_id)})
        return result.deleted_count > 0

    def like(self, comment_id: str, user_id: str) -> bool:
        # Optional: prevent multiple likes from same user using a "liked_by" field
        result = self.collection.update_one(
            {"_id": ObjectId(comment_id)},
            {"$inc": {"like_count": 1}}
        )
        return result.modified_count > 0
