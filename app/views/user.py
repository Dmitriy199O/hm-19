from flask import request
from flask_restx import Namespace, Resource
from app.container import user_service
from app.dao.models.user import UserSchema
from app.decorators import auth_required, admin_required

user_ns = Namespace('users')

users_schema = UserSchema(many=True)
user_schema = UserSchema()


@user_ns.route('/')
class UserView(Resource):
    def get(self):
        all_users = user_service.get_all()
        return users_schema.dump(all_users), 200

    def post(self):
        data = request.get_json()
        user_service.create(data)
        return "", 201


@user_ns.route('/<int:uid>')
class UserView(Resource):
    @auth_required
    def get_by_username(self, username):
        user = user_service.get_by_username(username)
        return user_schema.dumps(user), 200

    @auth_required
    @admin_required
    def put(self, uid):
        data = request.get_json()
        data['uid'] = uid
        user_service.update(data)
        return '', 204
