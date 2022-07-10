from app.dao.genre import GenreDAO


class GenreService:
    def __init__(self, dao: GenreDAO):
        self.dao = dao

    def get_one(self, gid):
        return self.dao.get_one(gid)

    def get_all(self):
        return self.dao.get_all()

    def create(self, data):
        self.dao.create(data)

    def update(self, data):
        gid = data.get("id")
        genre = self.dao.get_one(gid)
        genre.name = data.get('name')
        self.dao.update(genre)

    def update_partial(self, data):
        gid = data.get("id")
        genre = self.dao.get_one(gid)
        if 'name' in data:
            genre.description = data.get('name')

        self.dao.update(genre)

    def delete(self, gid):
        self.dao.delete(gid)
