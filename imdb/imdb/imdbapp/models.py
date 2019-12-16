from django.db import models
import csv
# Create your models here.

# from . populatedata import populate


class Movies(models.Model):
    movie_name = models.CharField(max_length=255)
    movie_runtime = models.IntegerField()
    movie_genre = models.CharField(max_length=255)
    movie_rating = models.FloatField()


file = open('imdbapp/topmovies.csv', 'r',newline='')
reader = csv.reader(file)
for row in reader:
    movie_name = row[0]
    movie_runtime = row[1]
    movie_genre = row[2]
    movie_rating = row[3]

    newrow = Movies(movie_name=movie_name,movie_runtime=movie_runtime,movie_genre=movie_genre,movie_rating=movie_rating)
    newrow.save()