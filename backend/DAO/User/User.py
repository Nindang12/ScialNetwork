from datetime import datetime

class User:
    def __init__(self, userID, username, email, phoneNumber, password, avatarURL, createdAt=None):
        self.userID = userID
        self.username = username
        self.email = email
        self.phoneNumber = phoneNumber
        self.password = password
        self.avatarURL = avatarURL
        self.createdAt = createdAt or datetime.utcnow()

    def to_json(self):
        return {
            "_id": self.userID,
            "username": self.username,
            "email": self.email,
            "phoneNumber": self.phoneNumber,
            "password": self.password,
            "avatarURL": self.avatarURL,
            "createdAt": self.createdAt.strftime("%Y-%m-%d %H:%M:%S")
        }

    @staticmethod
    def from_json(data):
        return User(
            userID=data["_id"],
            username=data["username"],
            email=data["email"],
            phoneNumber=data["phoneNumber"],
            password=data["password"],
            avatarURL=data["avatarURL"],
            createdAt=datetime.strptime(data["createdAt"], "%Y-%m-%d %H:%M:%S")
        )
