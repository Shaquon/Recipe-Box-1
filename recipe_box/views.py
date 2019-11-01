from django.shortcuts import render,HttpResponseRedirect, reverse
from django.utils import timezone
from recipe_box.models import Recipe, Chef
from recipe_box.forms import RecipeAddForm, ChefAddForm

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


def chefaddview(request):
    html = "generic_form.html"

    form = ChefAddForm()
    if request.method == 'POST':
        form = ChefAddForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            Chef.objects.create(
                name=data['name'],
                bio=data['bio']
                )
            return HttpResponseRedirect(reverse('recipeadd'))
    return render(request, html, {'form': form})


def recipeaddview(request):
    html = "generic_form.html"
    form  = RecipeAddForm()
    if request.method == 'POST':
        form = RecipeAddForm(request.POST)
        form.save()
        return HttpResponseRedirect(reverse('homepage'))

    return render(request, html, {'form': form})