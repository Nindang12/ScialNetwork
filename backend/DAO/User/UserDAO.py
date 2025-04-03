from pymongo import MongoClient
from User import User

class UserDAO:
    def __init__(self, db_url="mongodb://localhost:27017/", db_name="mydatabase"):
        self.client = MongoClient(db_url)
        self.db = self.client[db_name]
        self.collection = self.db["users"]

    def getAll(self):
        users = self.collection.find({})
        return [User.from_json(user) for user in users]

    def get(self, user_id):
        user = self.collection.find_one({"_id": user_id})
        return User.from_json(user) if user else None

    def findByEmail(self, email):
        user = self.collection.find_one({"email": email})
        return User.from_json(user) if user else None

    def findByName(self, username):
        users = self.collection.find({"username": username})
        return [User.from_json(user) for user in users]

    def findByPhone(self, phone):
        user = self.collection.find_one({"phoneNumber": phone})
        return User.from_json(user) if user else None

    def add(self, user):
        if self.collection.find_one({"_id": user.userID}):
            return False  # Tránh trùng ID
        self.collection.insert_one(user.to_json())
        return True

    def update(self, user_id, updated_user):
        result = self.collection.update_one(
            {"_id": user_id},
            {"$set": updated_user.to_json()}
        )
        return result.modified_count > 0

    def delete(self, user_id):
        result = self.collection.delete_one({"_id": user_id})
        return result.deleted_count > 0
