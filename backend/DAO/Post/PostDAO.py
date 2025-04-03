from typing import List, Optional
from datetime import datetime
from Post import Post
from pymongo import MongoClient
from bson import ObjectId

class PostDAO:
    def __init__(self, db_url="mongodb://localhost:27017/", db_name="mydatabase"):
        self.client = MongoClient(db_url)
        self.db = self.client[db_name]
        self.collection = self.db['posts']

    def get_all(self) -> List[Post]:
        """Get all posts"""
        posts = self.collection.find()
        return [Post.create(post) for post in posts]

    def get(self, post_id: str) -> Optional[Post]:
        """Get a specific post by ID"""
        post = self.collection.find_one({"_id": ObjectId(post_id)})
        return Post.create(post) if post else None

    def add(self, post: Post) -> str:
        """Add a new post and return its ID"""
        try:
            post_dict = post.to_json()
            result = self.collection.insert_one(post_dict)
            return str(result.inserted_id)
        except Exception as e:
            print(f"Error adding post: {e}")
            return None

    def update(self, post_id: str, updated_post: Post) -> bool:
        """Update an existing post"""
        try:
            result = self.collection.update_one(
                {"_id": ObjectId(post_id)},
                {"$set": updated_post.to_json()}
            )
            return result.modified_count > 0
        except Exception as e:
            print(f"Error updating post: {e}")
            return False

    def delete(self, post_id: str) -> bool:
        """Delete a post"""
        try:
            result = self.collection.delete_one({"_id": ObjectId(post_id)})
            return result.deleted_count > 0
        except Exception as e:
            print(f"Error deleting post: {e}")
            return False

    def like(self, post_id: str, user_id: str) -> bool:
        """Like a post"""
        try:
            result = self.collection.update_one(
                {"_id": ObjectId(post_id)},
                {"$addToSet": {"likes": user_id}}
            )
            return result.modified_count > 0
        except Exception as e:
            print(f"Error liking post: {e}")
            return False

    def repost(self, post_id: str, user_id: str) -> bool:
        """Repost a post"""
        try:
            result = self.collection.update_one(
                {"_id": ObjectId(post_id)},
                {"$addToSet": {"reposts": user_id}}
            )
            return result.modified_count > 0
        except Exception as e:
            print(f"Error reposting: {e}")
            return False
