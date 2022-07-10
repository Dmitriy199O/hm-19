from flask import request, jsonify
from flask_restx import Namespace, Resource
from app.container import genre_service
from app.dao.models.genre import GenreSchema
from app.decorators import auth_required, admin_required

genre_ns = Namespace('genres')

genres_schema = GenreSchema(many=True)
genre_schema = GenreSchema()


@genre_ns.route('/')
class GenreView(Resource):
    @auth_required
    def get(self):
        all_genres = genre_service.get_all()

        return genres_schema.dump(all_genres), 200

    def post(self):
        data = request.get_json()
        genre_service.create(data)
        genre_id= data['id']
        response = jsonify()
        response.status_code = 201
        response.headers['location'] = f'/{genre_id}'
        return response


@genre_ns.route('/<int:gid>')
class GenreView(Resource):
    @auth_required
    def get(self, gid):
        genre = genre_service.get_one(gid)

        return genre_schema.dump(genre), 200

    @auth_required
    @admin_required
    def put(self, gid):
        data = request.json
        data['id'] = gid
        genre_service.update(data)

        return '', 204

    @auth_required
    @admin_required
    def patch(self, gid):
        data = request.json
        data['id'] = gid
        genre_service.update(data)
        return '', 204

    @auth_required
    @admin_required
    def delete(self, gid):
        genre_service.delete(gid)

        return '', 204
