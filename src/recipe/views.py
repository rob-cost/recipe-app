from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Recipe
from django.contrib.auth.models import User


def homepage_view(request):
    return render(request, 'recipe/homepage.html')

def recipes_view(request):
    recipes = Recipe.objects.all()
    print(f'Recipes count: {recipes.count()}')
    return render(request, 'recipe/recipes.html', {'recipes': recipes})

# @login_required
def recipe_details(request, recipe_id):
    user = request.user
    recipe = get_object_or_404(Recipe, id = recipe_id)
    ingredients = [i.strip() for i in recipe.ingredients.split(",") if i.strip()]
    likes_count = recipe.liked_by.count()
    print(f'Recipe liked by: {likes_count}')

    if recipe.liked_by.filter(id=user.id).exists():
        user_has_liked = True
    else:
        user_has_liked = False

    context = {
        'recipe': recipe,
        'ingredients': ingredients,
        'total_likes': likes_count,
        'user_has_liked': user_has_liked
    }

    return render(request,'recipe/recipe_details.html', context)

def toggle_like(request, recipe_id):
    user = request.user
    recipe = get_object_or_404(Recipe, id = recipe_id)

    if request.method == "POST":
        if recipe.liked_by.filter(id=user.id).exists():
            recipe.liked_by.remove(user)
        else:
            recipe.liked_by.add(user)
    
    return redirect('recipe_details', recipe_id = recipe_id)




