from typing import List, Optional
from bson.objectid import ObjectId
from user import User
from dao_interface import IUserDAO
import logging

class DatabaseError(Exception):
    pass

class UserDAO(IUserDAO):
    def __init__(self, db):
        self.db = db
        self.collection = self.db["users"]
        self.logger = logging.getLogger(__name__)

    def getAll(self) -> List[User]:
        try:
            users = self.collection.find()
            return [User(**user) for user in users]
        except Exception as e:
            self.logger.error(f"Error getting all users: {str(e)}")
            raise DatabaseError(f"Error getting all users: {str(e)}")

    def get(self, user_id: str) -> Optional[User]:
        try:
            user = self.collection.find_one({"_id": ObjectId(user_id)})
            return User(**user) if user else None
        except Exception as e:
            self.logger.error(f"Error getting user {user_id}: {str(e)}")
            raise DatabaseError(f"Error getting user {user_id}: {str(e)}")

    def findByEmail(self, email: str) -> Optional[User]:
        try:
            user = self.collection.find_one({"email": email})
            return User(**user) if user else None
        except Exception as e:
            self.logger.error(f"Error finding user by email {email}: {str(e)}")
            raise DatabaseError(f"Error finding user by email {email}: {str(e)}")

    def add(self, user: User) -> bool:
        try:
            if not user.is_valid():
                self.logger.warning("Attempted to add invalid user")
                return False
                
            result = self.collection.insert_one(user.__dict__)
            return bool(result.inserted_id)
        except Exception as e:
            self.logger.error(f"Error adding user: {str(e)}")
            raise DatabaseError(f"Error adding user: {str(e)}")

    def update(self, user_id: str, updated_user: User) -> bool:
        try:
            if not updated_user.is_valid():
                self.logger.warning("Attempted to update user with invalid data")
                return False
                
            result = self.collection.update_one(
                {"_id": ObjectId(user_id)},
                {"$set": updated_user.__dict__}
            )
            return result.modified_count > 0
        except Exception as e:
            self.logger.error(f"Error updating user {user_id}: {str(e)}")
            raise DatabaseError(f"Error updating user {user_id}: {str(e)}")

    def delete(self, user_id: str) -> bool:
        try:
            result = self.collection.delete_one({"_id": ObjectId(user_id)})
            return result.deleted_count > 0
        except Exception as e:
            self.logger.error(f"Error deleting user {user_id}: {str(e)}")
            raise DatabaseError(f"Error deleting user {user_id}: {str(e)}")
