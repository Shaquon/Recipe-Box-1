from django.shortcuts import render

from recipe_box.models import Recipe,Chef

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

    chef = Chef.objects.filter(id=id).first()
    recipes = Recipe.objects.filter(chef=chef)
    

    return render(request, html, {"chef": chef, "recipes": recipes})