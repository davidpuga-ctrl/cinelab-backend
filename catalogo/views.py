from rest_framework import viewsets
from .models import Director, Pelicula
from .serializers import DirectorSerializer, PeliculaSerializer

class DirectorViewSet(viewsets.ModelViewSet):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer

class PeliculaViewSet(viewsets.ModelViewSet):
    queryset = Pelicula.objects.all()
    serializer_class = PeliculaSerializer