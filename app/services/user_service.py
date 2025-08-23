from app.repositories.user_repository import UserRepository
from app.models.user import User

class UserService:
    @staticmethod
    def list_users():
        return UserRepository.get_all()

    @staticmethod
    def create_user(name, email):
        user = User(name=name, email=email)
        return UserRepository.save(user)