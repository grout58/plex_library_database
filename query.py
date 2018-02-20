from plex_model import *


database.connect()


def search():
    print('Movie Title:')
    movie_search = input('> ')

    movies = Movies.select().where(Movies.sort_title.contains(movie_search))

    for movie in movies:
        print('Title: {}'.format(movie.sort_title))
        print('Summary: {}'.format(movie.summary))
        print('-' * 40)

while True:
    search()

