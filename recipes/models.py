from django.db import models


class Recipe(models.Model):
    name = models.CharField(max_length=255)
    ingredients = models.TextField()
    method = models.TextField()
    prep_time = models.IntegerField()
    servings = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
