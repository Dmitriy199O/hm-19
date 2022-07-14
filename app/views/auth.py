from flask import request, abort
from flask_restx import Namespace, Resource
from app.container import auth_service

auth_ns = Namespace('auth')


@auth_ns.route('/')
class AuthView(Resource):
    def post(self):
        data = request.get_json()
        username = data.get("username", None)
        password = data.get("password", None)

        if None in [username, password]:
            abort(400)

        tokens = auth_service.generate_tokens(username, password)

        return tokens, 201

    def put(self):
        data = request.get_json()

        token = data.get("refresh_token")

        tokens = auth_service.approve_token(token)

        return tokens, 201
