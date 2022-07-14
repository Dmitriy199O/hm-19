import calendar
import datetime
import jwt

from app.constants import JWT_SECRET, JWT_ALGORITHM
from app.dao.services.user import UserService
from flask import abort


class AuthService:
    def __init__(self, user_service: UserService):
        self.user_service = user_service

    def generate_tokens(self, username, password, is_refresh=False):
        user = self.user_service.get_by_username(username)

        if user is None:
            return "User not found", 404

        if not is_refresh:

            if not self.user_service.compare_passwords(user.password, password):
                return "Passwords do not match", 404

        data = {
            "username": username,
            "role": user.role
        }

        min30 = datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
        data['exp'] = calendar.timegm(min30.timetuple())
        access_token = jwt.encode(data, JWT_SECRET, algorithm=JWT_ALGORITHM)

        days130 = datetime.datetime.utcnow() + datetime.timedelta(days=30)
        data['exp'] = calendar.timegm(days130.timetuple())
        refresh_token = jwt.encode(data, JWT_SECRET, algorithm=JWT_ALGORITHM)

        token = {
            "access_token": access_token,
            "refresh_token": refresh_token
        }
        return token, 201

    def approve_token(self, refresh_token):
        data = jwt.decode(jwt=refresh_token, key=JWT_SECRET, algorithms=[JWT_ALGORITHM])
        username = data.get('username')
        user = self.user_service.get_by_username(username)
        if not user:
            raise Exception
        return self.generate_tokens(user.username, user.password, is_refresh=True)
