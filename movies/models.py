from django.db import models

# Create your models here.


class Movie(models.Model):
    year = models.IntegerField()
    title = models.TextField()
    origin = models.TextField()
    director = models.TextField()
    cast = models.TextField()
    genre = models.TextField()
    wikipage = models.TextField()
    plot = models.TextField()

    def __str__(self):
        return self.title
