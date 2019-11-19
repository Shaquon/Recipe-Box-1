from django import forms
from recipe_box.models import Recipe, Chef
from django.contrib.auth.models import User

class ChefAddForm(forms.Form):
    name = forms.CharField(max_length=50)
    bio = forms.CharField(widget=forms.Textarea)



class RecipeAddForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = [
            'chef',
            'recipe_name',
            'ingredients',
            'steps',
            'time_required'
        ]

class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)

class SignUpForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)