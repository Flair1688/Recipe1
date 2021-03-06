from django import forms
from .models import Recipe

class AddRecipeForm(forms.ModelForm):

    class Meta:
        model = Recipe
        fields = ('title', 'description', 'video', 'image', 'number', 'ingredient', 'gram', 'cooking', 'category')
