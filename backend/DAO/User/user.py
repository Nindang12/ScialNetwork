from datetime import datetime
import json
import re
from user_interface import IUser
import logging

class User(IUser):
    def __init__(self, username: str, email: str, phoneNumber: str, password: str, avatarURL: str):
        if not self._validate_email(email):
            raise ValueError("Invalid email format")
        if not self._validate_password(password):
            raise ValueError("Password must be at least 8 characters")
            
        self.user_id = None
        self.username = username
        self.email = email
        self.phoneNumber = phoneNumber
        self.password = password
        self.avatarURL = avatarURL
        self.createdAt = datetime.utcnow()

    def _validate_email(self, email: str) -> bool:
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return bool(re.match(pattern, email))

    def _validate_password(self, password: str) -> bool:
        return len(password) >= 8

    def is_valid(self) -> bool:
        return all([
            self.username,
            self._validate_email(self.email),
            self._validate_password(self.password),
            self.avatarURL
        ])

    def to_json(self) -> str:
        """Convert user object to JSON."""
        return json.dumps(self.__dict__, default=str)

    def create(self, user_dict: dict) -> bool:
        """Create a user from a dictionary."""
        try:
            self.user_id = user_dict.get("user_id")
            self.username = user_dict.get("username")
            self.email = user_dict.get("email")
            self.phoneNumber = user_dict.get("phoneNumber")
            self.password = user_dict.get("password")
            self.avatarURL = user_dict.get("avatarURL")
            self.createdAt = user_dict.get("createdAt", datetime.utcnow())
            return self.is_valid()
        except Exception as e:
            logging.error(f"Error creating user: {str(e)}")
            return False
