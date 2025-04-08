from abc import ABC, abstractmethod
from user import User

class IUserDAO(ABC):
    @abstractmethod
    def getAll(self) -> list:
        pass

    @abstractmethod
    def get(self, user_id: str) -> User:
        pass

    @abstractmethod
    def findByEmail(self, email: str) -> User:
        pass

    @abstractmethod
    def add(self, user: User) -> bool:
        pass

    @abstractmethod
    def update(self, user_id: str, updated_user: User) -> bool:
        pass

    @abstractmethod
    def delete(self, user_id: str) -> bool:
        pass
