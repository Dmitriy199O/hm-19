from app.dao.models.user import User


class UserDAO:
    def __init__(self, session):
        self.session = session

    def get_all(self):
        return self.session.query(User).all()

    def get_by_username(self, username):
        user = self.session.query(User).filter(User.username == username).first()
        return user

    def create(self, data):
        new_user = User(**data)

        self.session.add(new_user)
        self.session.commit()

        return new_user

