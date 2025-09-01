from django import forms
from .models import Cat, Food

class CatForm(forms.ModelForm):
    class Meta:
        model = Cat
        fields = ["name", "breed", "age", "description", "is_alive"]

class FoodForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = ['name', 'brand', 'description', 'cat']
