from unicodedata import name
from django.db import models

class Musicdata(models.Model):
    acousticness = models.FloatField()
    artists = models.TextField()
    danceability = models.FloatField()
    duration_ms = models.FloatField()
    energy = models.FloatField()
    explicit = models.FloatField()
    id = models.TextField(primary_key=True)
    instrumentalness = models.FloatField()
    key = models.FloatField()
    liveness = models.FloatField()
    loudness = models.FloatField()
    mode = models.FloatField()
    name = models.TextField()
    popularity = models.FloatField()
    release_date = models.IntegerField()
    speechiness = models.FloatField()
    tempo = models.FloatField()
    valence = models.FloatField()
    year = models.IntegerField()

class Artistdata(models.Model):
    id = models.TextField(primary_key=True)
    followers = models.IntegerField()
    genres = models.TextField()
    name = models.TextField()
    popularity = models.IntegerField()