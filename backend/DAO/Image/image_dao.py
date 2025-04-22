from bson.objectid import ObjectId
from image import Image
from typing import List

class ImageDAO:
    def __init__(self, db):
        self.db = db
        self.collection = self.db["images"]

    def getAll(self) -> list:
        images = self.collection.find()
        return [Image(**img) for img in images]

    def get(self, image_id: str) -> Image:
        img = self.collection.find_one({"_id": ObjectId(image_id)})
        return Image(**img) if img else None

    def getByPost(self, post_id: str) -> list:
        images = self.collection.find({"post_id": post_id})
        return [Image(**img) for img in images]

    def add(self, image: Image) -> bool:
        result = self.collection.insert_one(image.__dict__)
        return bool(result.inserted_id)

    def update(self, image_id: str, updated_image: Image) -> bool:
        result = self.collection.update_one(
            {"_id": ObjectId(image_id)},
            {"$set": updated_image.__dict__}
        )
        return result.modified_count > 0

    def delete(self, image_id: str) -> bool:
        try:
            result = self.collection.delete_one({"_id": ObjectId(image_id)})
            return result.deleted_count > 0
        except Exception as e:
            self.logger.error(f"Error deleting image {image_id}: {str(e)}")

    def getByUser(self, user_id: str) -> List[Image]:
        try:
            images = self.collection.find({"user_id": user_id})
            return [Image(**img) for img in images]
        except Exception as e:
            self.logger.error(f"Error getting images for user {user_id}: {str(e)}")
