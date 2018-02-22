from plex_model import *
import os

movie_list = []
count = 0
done = False


def clear_screen():
    os.system('cls' if os.name =='nt' else 'clear')

## search db and add data to list of dictionaries.
def db_search(movie_title):
    database.connect()
    for record in Movies.select().where(Movies.sort_title.contains(movie_title)):
        movie_list.append({record.sort_title: {'Duration': record.duration,
            'Content Rating': record.content_rating, 'Summary': record.summary}})

    database.close()


def print_list():
    clear_screen()
    print('Results for: {}'.format(movie_title))
    for k, v in movie_list[count].items():
        print('Title:', k)
        print('Duration:', v['Duration'])
        print('Content Rating:', v['Content Rating'])
        print('\n')
        print('Summary:', v['Summary'])
        print('\n')
        print('{} out of {}'.format(count + 1, len(movie_list)))
        print('-' * 40)


def next_record():
    global count
    try:
        count += 1
        print_list()
    except IndexError:
        print('Out of movies')


def prev_record():
    global count
    try:
        count -= 1
        print_list()
    except IndexError:
        print("Out of movies")


def new_movie():
    global movie_list
    del movie_list
    movie_list = []


## menu system that gives pages and a way to scroll the pages
while not done:
    print("""
Search movie title to get movie info.
N) for next movie
P) for previous movie
Q) to quit
------------------------------------------
""")
    movie_title = input('> ').upper()
    if movie_title == 'Q':
        done = True
    elif movie_title == 'N':
        next_record()
    elif movie_title == 'P':
        prev_record()
    elif movie_title == 'M':
        new_movie()
    else:
        db_search(movie_title)
        print_list()
