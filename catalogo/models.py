from django.db import models

class Director(models.Model):
    nombre = models.CharField(max_length=100)
    nacionalidad = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='directores/', null=True, blank=True) 

    def __str__(self):
        return self.nombre

class Pelicula(models.Model):
    titulo = models.CharField(max_length=200)
    estreno = models.IntegerField()
    director = models.ForeignKey(Director, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='peliculas/', null=True, blank=True)
    sinopsis = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.titulo