from pymongo import MongoClient
from bson.objectid import ObjectId
from image import Image

class ImageDAO:
    def __init__(self, db_url="mongodb://localhost:27017/", db_name="imageDB"):
        self.client = MongoClient(db_url)
        self.db = self.client[db_name]
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
