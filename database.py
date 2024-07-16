from peewee import *

db = SqliteDatabase("reviews.db")

class Filme(Model):
    nome = CharField(unique = True)
    nota = DecimalField()
    review = TextField()

    class Meta:
        database = db

class Serie(Model):
    nome = CharField(unique = True)
    nota = DecimalField()
    review = TextField()

    class Meta:
        database = db