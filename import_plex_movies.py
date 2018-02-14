"""
Script imports Plex Media Library from CSV to Sqlite Database

Author: Jason Grout
Date 02/14/2018

"""

import csv

from peewee import *


db = SqliteDatabase('plex_library.db')


class Movies(Model):
    media_id = CharField(max_length=255)
    title = CharField(max_length=255)
    sort_title = CharField(max_length=255)
    studio = CharField(max_length=255)
    content_rating = CharField(max_length=255)
    year = CharField(max_length=255)
    rating = CharField(max_length=255)
    summary = CharField(max_length=255)
    genres = CharField(max_length=255)
    view_count = CharField(max_length=255)
    last_viewed_at = CharField(max_length=255)
    tagline = CharField(max_length=255)
    release_date = CharField(max_length=255)
    writers = CharField(max_length=255)
    country = CharField(max_length=255)
    duration = CharField(max_length=255)
    directors = CharField(max_length=255)
    roles = CharField(max_length=255)

    class Meta:
        database = db


def initialize():
    db.connect()
    db.create_tables([Movies], safe=True)


def menu():
    print("m) to create matrix")
    print("q) to quit")
    choice = input("> ")
    if choice == 'm':
        create_db()
    elif choice == "q":
        exit()


def create_db():
    with open('movies.csv', newline='') as csvfile:
        plexreader = csv.DictReader(csvfile, delimiter=',')
        rows = list(plexreader)
        for row in rows[:]:
            Movies.create(media_id=row['Media ID'],
                          title=row['Title'], sort_title=row['Sort title'],
                          studio=row['Studio'], content_rating=row['Content Rating'],
                          year=row['Year'], rating=row['Rating'],
                          summary=row['Summary'], genres=row['Genres'],
			  view_count=row['View Count'], last_viewed_at=row['Last Viewed at'],
			  tagline=row['Tagline'], release_date=row['Release Date'],
			  writers=row['Writers'], country=row['Country'],
			  duration=row['Duration'], directors=row['Directors'],
                          roles=row['Roles'])


if __name__ == '__main__':
    initialize()
    menu()
