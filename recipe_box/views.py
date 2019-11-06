from django.shortcuts import render,HttpResponseRedirect, reverse, HttpResponse
from django.utils import timezone
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from recipe_box.models import Recipe, Chef
from recipe_box.forms import RecipeAddForm, ChefAddForm, LoginForm, SignUpForm

def index(request):
    html = "index.html"
    
    recipe = Recipe.objects.all()

    return render(request, html, {"data": recipe})

def recipe_detail(request, id):
    html = "recipe.html"
    recipe = Recipe.objects.filter(id=id).first()
    ingredients, steps = recipe.ingredients, recipe.steps
    if '.' in ingredients or steps:
        ingredients = recipe.ingredients.split(".")
        steps = recipe.steps.split('.')
    

    return render(request, html, {"ingredients": ingredients, "steps": steps, "recipe": recipe})


def chef_detail(request, id):
    html = "chef.html"

    chef = Chef.objects.filter(id=id).first()
    recipes = Recipe.objects.filter(chef=chef)
    
    return render(request, html, {"chef": chef, "recipes": recipes})


@login_required
def chefaddview(request):
    html = "generic_form.html"
    form = ChefAddForm()
    if request.user.is_staff:
        if request.method == 'POST':
            form = ChefAddForm(request.POST)
            if form.is_valid():
                data = form.cleaned_data
                u = User.objects.create_user(
                    username=data['name']
                )
                Chef.objects.create(
                    user=u,
                    name=data['name'],
                    bio=data.get('bio')
                    )
                return HttpResponseRedirect(reverse('recipeadd'))
    else:
        return HttpResponse("Nah homie.  You don't have the proper credentials")
    return render(request, html, {'form': form})

@login_required
def recipeaddview(request):
    html = "generic_form.html"
    form  = RecipeAddForm()
    if request.method == 'POST':
        form = RecipeAddForm(request.POST)
        form.save()
        return HttpResponseRedirect(reverse('homepage'))

    return render(request, html, {'form': form})


def login_view(request):
    html = "generic_form.html"

    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            if user := authenticate(
                username=data['username'],
                password=data['password']
            ):
                login(request, user)
                # breakpoint()
                return HttpResponseRedirect(request.GET.get('next', '/'))

    return render(request, html, {'form': form})


def sign_up_view(request):
    html = "generic_form.html"
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            User.objects.create_user(
                username=data['username'],
                password=data['password']
                )
            if user := authenticate(
                username=data['username'],
                password=data['password']
            ):
                login(request, user)
            return HttpResponseRedirect(reverse('homepage'))

    return render(request, html, {'form': form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('homepage'))