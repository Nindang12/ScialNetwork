from bson.objectid import ObjectId
from user import User

class UserDAO:
    def __init__(self, db):
        self.db = db
        self.collection = self.db["users"]

    def getAll(self) -> list:
        """Retrieve all users from the database."""
        users = self.collection.find()
        return [User(**user) for user in users]

    def get(self, user_id: str) -> User:
        """Retrieve a user by their ID."""
        user = self.collection.find_one({"_id": ObjectId(user_id)})
        return User(**user) if user else None

    def findByEmail(self, email: str) -> User:
        """Find a user by their email."""
        user = self.collection.find_one({"email": email})
        return User(**user) if user else None

    def add(self, user: User) -> bool:
        """Add a new user to the database."""
        result = self.collection.insert_one(user.__dict__)
        return bool(result.inserted_id)

    def update(self, user_id: str, updated_user: User) -> bool:
        """Update an existing user in the database."""
        result = self.collection.update_one(
            {"_id": ObjectId(user_id)},
            {"$set": updated_user.__dict__}
        )
        return result.modified_count > 0

    def delete(self, user_id: str) -> bool:
        """Delete a user from the database."""
        result = self.collection.delete_one({"_id": ObjectId(user_id)})
        return result.deleted_count > 0
