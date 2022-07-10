from app.create_db import db
from app.dao.movie import MovieDAO
from app.dao.genre import GenreDAO
from app.dao.director import DirectorDAO
from app.dao.services.auth import AuthService
from app.dao.services.movie import MovieService
from app.dao.services.genre import GenreService
from app.dao.services.director import DirectorService
from app.dao.services.user import UserService
from app.dao.user import UserDAO

movie_dao = MovieDAO(db.session)
movie_service = MovieService(movie_dao)

genre_dao = GenreDAO(db.session)
genre_service = GenreService(genre_dao)

director_dao = DirectorDAO(db.session)
director_service = DirectorService(director_dao)

user_dao = UserDAO(db.session)
user_service = UserService(user_dao)

auth_service = AuthService(user_service)
