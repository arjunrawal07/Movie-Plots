from rest_framework import serializers
from .models import Movie


class MovieSerializer(serializers.ModelSerializer):
    model = Movie
    fields = ('year',
              'title',
              'origin',
              'director',
              'cast',
              'genre',
              'wikipage',
              'plot')
