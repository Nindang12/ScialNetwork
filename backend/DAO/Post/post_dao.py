from pymongo import MongoClient
from bson.objectid import ObjectId
from post import Post

class PostDAO:
    def __init__(self, db_url="mongodb://localhost:27017/", db_name="postDB"):
        self.client = MongoClient(db_url)
        self.db = self.client[db_name]
        self.collection = self.db["posts"]

    def getAll(self) -> list:
        posts = self.collection.find()
        return [Post(**p) for p in posts]

    def get(self, post_id: str) -> Post:
        post = self.collection.find_one({"_id": ObjectId(post_id)})
        return Post(**post) if post else None

    def add(self, post: Post) -> bool:
        result = self.collection.insert_one(post.__dict__)
        return bool(result.inserted_id)

    def update(self, post_id: str, updated_post: Post) -> bool:
        result = self.collection.update_one(
            {"_id": ObjectId(post_id)},
            {"$set": updated_post.__dict__}
        )
        return result.modified_count > 0

    def delete(self, post_id: str) -> bool:
        result = self.collection.delete_one({"_id": ObjectId(post_id)})
        return result.deleted_count > 0

    def like(self, post_id: str, user_id: str) -> bool:
        # Example: increment a "likes" field, or store user_id in a "likes" array
        result = self.collection.update_one(
            {"_id": ObjectId(post_id)},
            {"$addToSet": {"likes": user_id}}  # Avoid duplicates
        )
        return result.modified_count > 0

    def repost(self, post_id: str, user_id: str) -> bool:
        # Copy post with new user_id and current time
        original = self.get(post_id)
        if not original:
            return False
        repost = Post(
            userID=user_id,
            video_id=original.video_id,
            image_id=original.image_id,
            content=original.content
        )
        return self.add(repost)
