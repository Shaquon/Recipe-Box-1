"""
Chef
    Name


Recipes
    Date
    Recipe Name
    Ingredients
    Steps
    chef
"""
from django.db import models

class Chef(models.Model):
    name = models.CharField(max_length=50)
    bio = models.TextField()
    def __str__(self):
        return f"{self.name}"

class Recipe(models.Model):
    chef = models.ForeignKey(Chef, on_delete=models.CASCADE)
    date = models.DateTimeField()
    recipe_name = models.CharField(max_length=50)
    ingredients = models.TextField()
    steps = models.TextField()
    time_required = models.TextField()

    def __str__(self):
        return f"{self.recipe_name}"


