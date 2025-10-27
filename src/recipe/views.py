from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Recipe
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError




def login_view(request):

    if request.method == "POST":
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username = username, password = password)
            if user:
                login(request, user)
                return redirect('homepage')
        else:
            messages.error(request, 'Invalid username or password')
    
    form = AuthenticationForm()

    context = {
        'form': form,
    }
    return render(request, 'auth/login.html', context)
    
def logout_view(request):
    logout(request)
    messages.success(request, 'You have successfuly logged out!')
    return redirect('login')

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Automatically hashes the password
            login(request, user)  
            return redirect('homepage')
    else:
        form = UserCreationForm()

    return render(request, 'auth/signup.html', {'form': form})

def homepage_view(request):
    recipes = Recipe.objects.all()
    popular_recipes = []
    for recipe in recipes:
        recipe_likes_count = recipe.liked_by.count()
        if recipe_likes_count >=1:
            popular_recipes.append(recipe)
    context = {
        'popular_recipes': popular_recipes
    }
    return render(request, 'recipe/homepage.html', context)

@login_required
def recipes_view(request):
    recipes = Recipe.objects.all()
    print(f'Recipes count: {recipes.count()}')
    return render(request, 'recipe/recipes.html', {'recipes': recipes})

@login_required
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

@login_required
def toggle_like(request, recipe_id):
    user = request.user
    recipe = get_object_or_404(Recipe, id = recipe_id)

    if request.method == "POST":
        if recipe.liked_by.filter(id=user.id).exists():
            recipe.liked_by.remove(user)
        else:
            recipe.liked_by.add(user)
    
    return redirect('recipe_details', recipe_id = recipe_id)




