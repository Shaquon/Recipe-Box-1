from django.shortcuts import render

from recipe_box.models import Recipe

def index(request):
    html = "index.html"
    
    recipe = Recipe.objects.all()

    return render(request, html, {"data": recipe})


def recipe_detail(request, id):
    html = "recipe.html"

    recipe = Recipe.objects.filter(id=id).first()
    ingredients = recipe.ingredients.split(".")[:-1]
    steps = recipe.steps.split(".")[:-1]

    return render(request, html, {"ingredients": ingredients, "steps": steps, "recipe": recipe})


def chef_detail(request, id):
    html = "chef.html"

    chefs = Recipe.objects.filter(id=id)
    recipes = Recipe.objects.filter(chef=id)

    return render(request, html, {"chefs": chefs, "recipes": recipes})