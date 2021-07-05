from django.shortcuts import render, get_object_or_404
from .models import Recipe


def index(request):
    recipes = Recipe.objects.all()
    data = {
        'recipes': recipes
    }
    return render(request, 'index.html', data)


def recipe(request, id):
    recipe = get_object_or_404(Recipe, pk=id)
    data = {
        'recipe': recipe
    }
    return render(request, 'receita.html', data)