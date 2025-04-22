from abc import ABC, abstractmethod
from typing import List, Optional
from user import User

class IUserDAO(ABC):
    @abstractmethod
    def getAll(self) -> List[User]:
        pass

    @abstractmethod
    def get(self, user_id: str) -> Optional[User]:
        pass

    @abstractmethod
    def findByEmail(self, email: str) -> Optional[User]:
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
