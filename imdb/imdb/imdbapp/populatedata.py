# import os

# os.environ['PYTHONPATH'] = 'imdb'
# os.environ['DJANGO_SETTINGS_MODULE'] = 'imdb/imdb/settings.py'


# import csv

# from imdbapp.models import Movies
# def populate():
#     file = open('imdbapp/topmovies.csv', 'r',newline='')
#     reader = csv.reader(file)
#     for row in reader:
#         movie_name = row[0]
#         movie_runtime = row[1]
#         movie_genre = row[2]
#         movie_rating = row[3]

#         newrow = Movies(movie_name=movie_name,movie_runtime=movie_runtime,movie_genre=movie_genre,movie_rating=movie_rating)
#         newrow.save()