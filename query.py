from plex_model import *


database.connect()

search = str(input('Movie Title: > '))

movies = Movies.select().where(Movies.sort_title.contains(search))

for movie in movies:
    print('Title: {}'.format(movie.sort_title))
    print('Summary: {}'.format(movie.summary))
    print('-' * 40)


