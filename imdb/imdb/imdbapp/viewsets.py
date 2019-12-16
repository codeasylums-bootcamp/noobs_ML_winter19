from rest_framework import viewsets
from . import models,serializers

class MoviesViewset(viewsets.ModelViewSet):
    queryset = models.Movies.objects.all()
    serializer_class = serializers.MoviesSerializer
    
    