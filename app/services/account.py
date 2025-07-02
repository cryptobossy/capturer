from app.database.account import UserDB
from app.sql import db
from sqlalchemy.exc import SQLAlchemyError
from app.models import UserBase
class UserService:
    """
    Service class for handling user-related operations.
    """

    @staticmethod
    def create_user(user_data:UserBase):
        """
        Create a new user.
        """
        try:
            user = UserDB()
            for key, value in user_data.model_dump().items():
                if value is not None:
                    setattr(user, key, value)
            db.session.add(user)
            db.session.commit()
            return user
        except SQLAlchemyError as e:
            db.session.rollback()
            raise e

    @staticmethod
    def read_user(user_id:int):
        """
        Retrieve an user by its ID.
        """
        data = db.session.get(UserDB, user_id)
        if data is None:
            return None
        # Construye el diccionario solo con los atributos públicos
        user_dict = {col.name: getattr(data, col.name) for col in data.__table__.columns}
        user = UserBase(**user_dict)
        return user

    @staticmethod
    def delete_user(user_id):
        """
        Delete an user by its ID.
        """
        try:
            user = db.session.get(UserDB, user_id)
        except AttributeError as e:
            return None
        if not user:
            return None
        try:
            db.session.delete(user)
            db.session.commit()
            return True
        except SQLAlchemyError as e:
            db.session.rollback()
            raise e

    @staticmethod
    def list_users():
        """
        List all users.
        """
        return UserDB.query.all()

    @staticmethod
    def get_user_by_name(name):
        """
        Get users by their name.
        """
        return UserDB.query.filter_by(name=name).all()
    @staticmethod
    def user_count():
        """
        Count the number of users.
        """
        return UserDB.query.count()
    @staticmethod
    def get_user_list():
        """
        Get a list of all users.
        """
        users = UserDB.query.all()
        user_list = []
        for user in users:
            user_dict = {col.name: getattr(user, col.name) for col in user.__table__.columns}
            user_list.append(UserBase(**user_dict))
        return user_list


