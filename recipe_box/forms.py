from django import forms
from recipe_box.models import Recipe, Chef

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
