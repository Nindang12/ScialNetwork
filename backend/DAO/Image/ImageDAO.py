from typing import List, Optional
from pymongo import MongoClient
from bson import ObjectId
from Image import Image

class ImageDAO:
    def __init__(self, db_url="mongodb://localhost:27017/", db_name="mydatabase"):
        self.client = MongoClient(db_url)
        self.db = self.client[db_name]
        self.collection = self.db["images"]

    def get_all(self) -> List[Image]:
        """Get all images"""
        images = self.collection.find()
        return [Image.create(image) for image in images]

    def get(self, image_id: str) -> Optional[Image]:
        """Get a specific image by ID"""
        image = self.collection.find_one({"_id": ObjectId(image_id)})
        return Image.create(image) if image else None

    def get_by_post(self, post_id: str) -> List[Image]:
        """Get images by post ID"""
        images = self.collection.find({"post_id": post_id})
        return [Image.create(image) for image in images]

    def get_by_comment(self, comment_id: str) -> List[Image]:
        """Get images by comment ID"""
        images = self.collection.find({"comment_id": comment_id})
        return [Image.create(image) for image in images]

    def add(self, image: Image) -> bool:
        """Add a new image"""
        try:
            image_dict = image.to_json()
            del image_dict['image_id']  # MongoDB sẽ tự tạo _id
            result = self.collection.insert_one(image_dict)
            image.image_id = str(result.inserted_id)  # Gán _id đã tạo vào image.image_id
            return True
        except Exception as e:
            print(f"Error adding image: {e}")
            return False

    def update(self, image_id: str, updated_image: Image) -> bool:
        """Update an existing image"""
        try:
            result = self.collection.update_one(
                {"_id": ObjectId(image_id)},
                {"$set": updated_image.to_json()}
            )
            return result.modified_count > 0
        except Exception as e:
            print(f"Error updating image: {e}")
            return False
