from django.shortcuts import render, get_object_or_404
from .models import Recipe


def index(request):
    latest = Recipe.objects.order_by('-id')[:5]
    ctx = {
        'latest_recipes': latest,
    }
    return render(request, 'recipes/index.html', ctx)


def recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    lines = recipe.definition.replace('\r', '').split('\n')
    ingredients = recipe.ingredients.values()
    ctx = {
        'recipe': recipe,
        'lines': lines,
        'ingredients': ingredients,
    }
    return render(request, 'recipes/recipe.html', ctx)
