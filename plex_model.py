from peewee import *

database = SqliteDatabase('plex_library.db', **{})

class UnknownField(object):
    def __init__(self, *_, **__): pass

class BaseModel(Model):
    class Meta:
        database = database

class Movies(BaseModel):
    content_rating = CharField()
    country = CharField()
    directors = CharField()
    duration = CharField()
    genres = CharField()
    last_viewed_at = CharField()
    rating = CharField()
    release_date = CharField()
    roles = CharField()
    sort_title = CharField()
    studio = CharField()
    summary = CharField()
    tagline = CharField()
    title = CharField()
    view_count = CharField()
    writers = CharField()
    year = CharField()

    class Meta:
        table_name = 'movies'

