from flask import request, abort
from flask_restx import Namespace, Resource
from app.container import auth_service, user_service

auth_ns = Namespace('auth')


@auth_ns.route('/')
class AuthView(Resource):
    def post(self):
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')

        if None in [username, password]:
            return "", 401

        tokens = auth_service.generate_tokens(username, password)

        return "oh yeah", tokens, 201

    def put(self):
        data = request.get_json()

        token = data.get('refresh_token')

        tokens = auth_service.approve_refresh_token(token)

        return tokens, 201
