import base64
import hashlib
import hmac

from app.constants import PWD_HASH_ITERATIONS, PWD_HASH_SALT

from app.dao.user import UserDAO


class UserService:
    def __init__(self, dao: UserDAO):
        self.dao = dao

    def get_all(self):
        return self.dao.get_all()

    def get_by_username(self, username):
        return self.dao.get_by_username(username)

    def get_hash(self, password):
        return base64.b64encode(
            hashlib.pbkdf2_hmac('sha256', password.encode('utf8'), PWD_HASH_SALT, PWD_HASH_ITERATIONS))

    def create(self, user):
        user['password'] = self.get_hash(user['password'])
        self.dao.create(user)

    def compare_passwords(self, password_hash, other_password):
        decoded_digest = base64.b64decode(password_hash)

        hash_digest = hashlib.pbkdf2_hmac(
            'sha256',
            other_password.encode('utf8'),
            PWD_HASH_SALT,
            PWD_HASH_ITERATIONS
        )

        return hmac.compare_digest(decoded_digest, hash_digest)
