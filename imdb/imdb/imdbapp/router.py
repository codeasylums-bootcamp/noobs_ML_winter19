from imdbapp import viewsets
from rest_framework import routers

router = routers.DefaultRouter()
router.register('imdbapp', viewsets.MoviesViewset)
