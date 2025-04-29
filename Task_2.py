class Movies:
    def __init__(self, movies=None):
        if movies is None:
            movies = []
        self.movies = movies

    def add_movie(self, movie):
        self.movies.append(movie)

class Comedy(Movies):
    def add_movie(self, movie):
        self.movies.append(movie)
        return f'Комедии: "{movie}"'

class Drama(Movies):
    def add_movie(self, movie):
        self.movies.append(movie)
        return f'Драммы: "{movie}"'

comedy = Comedy()
drama = Drama()
print(comedy.add_movie('Большой куш'))
print(drama.add_movie('Оружейный барон'))
