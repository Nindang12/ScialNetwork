from typing import List, Optional
from bson.objectid import ObjectId
from post import Post
from dao_interface import IPostDAO
import logging

class PostDAO(IPostDAO):
    def __init__(self, db):
        """Initialize PostDAO with database connection.
        
        Args:
            db: MongoDB database instance
        """
        self.db = db
        self.collection = self.db["posts"]
        self.logger = logging.getLogger(__name__)

    def getAll(self) -> List[Post]:
        """Retrieve all posts from the database.
        
        Returns:
            List[Post]: List of all posts in the database
            
        Raises:
            DatabaseError: If there is an error accessing the database
        """
        try:
            posts = self.collection.find()
            return [Post(**p) for p in posts]
        except Exception as e:
            self.logger.error(f"Error getting all posts: {str(e)}")

    def get(self, post_id: str) -> Optional[Post]:
        """Retrieve a post by its ID.
        
        Args:
            post_id (str): The ID of the post to retrieve
            
        Returns:
            Optional[Post]: The post if found, None otherwise
            
        Raises:
            DatabaseError: If there is an error accessing the database
        """
        try:
            post = self.collection.find_one({"_id": ObjectId(post_id)})
            return Post(**post) if post else None
        except Exception as e:
            self.logger.error(f"Error getting post {post_id}: {str(e)}")

    def add(self, post: Post) -> bool:
        """Add a new post to the database.
        
        Args:
            post (Post): The post to add
            
        Returns:
            bool: True if the post was added successfully, False otherwise
            
        Raises:
            DatabaseError: If there is an error accessing the database
        """
        try:
            if not post.is_valid():
                self.logger.warning("Attempted to add invalid post")
                return False
                
            result = self.collection.insert_one(post.__dict__)
            return bool(result.inserted_id)
        except Exception as e:
            self.logger.error(f"Error adding post: {str(e)}")

    def update(self, post_id: str, updated_post: Post) -> bool:
        """Update an existing post in the database.
        
        Args:
            post_id (str): The ID of the post to update
            updated_post (Post): The updated post data
            
        Returns:
            bool: True if the post was updated successfully, False otherwise
            
        Raises:
            DatabaseError: If there is an error accessing the database
        """
        try:
            if not updated_post.is_valid():
                self.logger.warning("Attempted to update post with invalid data")
                return False
                
            result = self.collection.update_one(
                {"_id": ObjectId(post_id)},
                {"$set": updated_post.__dict__}
            )
            return result.modified_count > 0
        except Exception as e:
            self.logger.error(f"Error updating post {post_id}: {str(e)}")

    def delete(self, post_id: str) -> bool:
        """Delete a post from the database.
        
        Args:
            post_id (str): The ID of the post to delete
            
        Returns:
            bool: True if the post was deleted successfully, False otherwise
            
        Raises:
            DatabaseError: If there is an error accessing the database
        """
        try:
            result = self.collection.delete_one({"_id": ObjectId(post_id)})
            return result.deleted_count > 0
        except Exception as e:
            self.logger.error(f"Error deleting post {post_id}: {str(e)}")

    def like(self, post_id: str, user_id: str) -> bool:
        """Add a like to a post.
        
        Args:
            post_id (str): The ID of the post to like
            user_id (str): The ID of the user who liked the post
            
        Returns:
            bool: True if the like was added successfully, False otherwise
            
        Raises:
            DatabaseError: If there is an error accessing the database
        """
        try:
            result = self.collection.update_one(
                {"_id": ObjectId(post_id)},
                {"$addToSet": {"likes": user_id}}  # Avoid duplicates
            )
            return result.modified_count > 0
        except Exception as e:
            self.logger.error(f"Error liking post {post_id} by user {user_id}: {str(e)}")

    def repost(self, post_id: str, user_id: str) -> bool:
        """Create a repost of an existing post.
        
        Args:
            post_id (str): The ID of the post to repost
            user_id (str): The ID of the user creating the repost
            
        Returns:
            bool: True if the repost was created successfully, False otherwise
            
        Raises:
            DatabaseError: If there is an error accessing the database
        """
        try:
            original = self.get(post_id)
            if not original:
                self.logger.warning(f"Attempted to repost non-existent post {post_id}")
                return False
                
            repost = Post(
                userID=user_id,
                video_id=original.video_id,
                image_id=original.image_id,
                content=original.content
            )
            
            if not repost.is_valid():
                self.logger.warning("Attempted to create invalid repost")
                return False
                
            return self.add(repost)
        except Exception as e:
            self.logger.error(f"Error reposting post {post_id} by user {user_id}: {str(e)}")
