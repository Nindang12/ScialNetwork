from datetime import datetime
import json

class User:
    def __init__(self, username: str, email: str, phoneNumber: str, password: str, avatarURL: str):
        self.userID = None  # This will be set when inserted into MongoDB
        self.username = username
        self.email = email
        self.phoneNumber = phoneNumber
        self.password = password
        self.avatarURL = avatarURL
        self.createdAt = datetime.utcnow()

    def to_json(self) -> str:
        """Convert user object to JSON."""
        return json.dumps(self.__dict__, default=str)

    def create(self, user_dict: dict) -> bool:
        """Create a user from a dictionary."""
        try:
            self.userID = user_dict.get("userID")
            self.username = user_dict.get("username")
            self.email = user_dict.get("email")
            self.phoneNumber = user_dict.get("phoneNumber")
            self.password = user_dict.get("password")
            self.avatarURL = user_dict.get("avatarURL")
            self.createdAt = user_dict.get("createdAt", datetime.utcnow())
            return True
        except Exception:
            return False
