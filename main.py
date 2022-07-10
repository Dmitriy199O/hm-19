from flask import Flask
from flask_restx import Api
from app.config import Config
from app.create_db import db
from app.add_data_to_db import add_data_to_db
from app.views.auth import auth_ns
from app.views.movies import movies_ns
from app.views.director import director_ns
from app.views.genres import genre_ns
from app.views.user import user_ns


def create_app(config: Config) -> Flask:
    app = Flask(__name__)
    app.config.from_object(config)
    app.app_context().push()
    return app


def configure_app(app: Flask):
    db.init_app(app)
    api = Api(app)
    api.add_namespace(movies_ns)
    api.add_namespace(director_ns)
    api.add_namespace(genre_ns)
    api.add_namespace(user_ns)
    api.add_namespace(auth_ns)


app_config = Config()
app = create_app(app_config)
configure_app(app)

if __name__ == '__main__':
    app_config = Config()
    app = create_app(app_config)
    configure_app(app)
    add_data_to_db(app, db)

    app.run()
