from app.container import user_service
from app.dao.models.user import User


def add_data_to_db(app, db):
    """
    This function is used to add default users to database with passwords already encoded
    :param app:
    :param db:

    """

    with app.app_context():
        db.create_all()

        u1 = User(username="vasya", password="my_little_pony", role="admin")
        u2 = User(username="oleg", password="qwerty", role="user")
        u3 = User(username="jesus", password="P@ssw0rd", role="user")
        u4 = User(username="stepplton", password="skypr0", role="user")
        u5 = User(username="hrooms", password="__rr11", role="admin")
        u6 = User(username="marie", password="1d1ot", role="admin")

        users = [u1, u2, u3, u4, u5, u6]
        for user in users:
            password = user.password
            encoded_password = user_service.get_hash(password)
            user.password = encoded_password

        with db.session.begin():
            db.session.add_all(users)
