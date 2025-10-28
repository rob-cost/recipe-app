from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import Recipe

class RecipeModelTest(TestCase):

    def test_difficulty_calculation_easy(self):
        recipe = Recipe(name="Salad", ingredients="lettuce, tomato", cooking_time=5, method="Test")
        recipe.full_clean()
        recipe.save()
        self.assertEqual(recipe.difficulty, "Easy")

    def test_difficulty_calculation_medium(self):
        recipe = Recipe(name="Soup", ingredients="water, carrot, potato, onion", cooking_time=5, method="Test")
        recipe.full_clean()
        recipe.save()
        self.assertEqual(recipe.difficulty, "Medium")

    def test_difficulty_calculation_intermediate(self):
        recipe = Recipe(name="Steak", ingredients="beef, salt", cooking_time=15, method="Test")
        recipe.full_clean()
        recipe.save()
        self.assertEqual(recipe.difficulty, "Intermediate")

    def test_difficulty_calculation_hard(self):
        recipe = Recipe(name="Lasagna", ingredients="pasta, cheese, tomato, beef", cooking_time=15, method="Test")
        recipe.full_clean()
        recipe.save()
        self.assertEqual(recipe.difficulty, "Hard")

class RecipesViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username = 'Roberto',
            password = 'ciaobellaitalia2025'
        )
        self.client.login(username="Roberto", password="ciaobellaitalia2025")

        Recipe.objects.create(
            name = 'Recipe_1',
            ingredients = 'ing-1, ing-2',
            cooking_time = 20,
            method = 'Test method 1'
        )
        Recipe.objects.create(
            name = 'Recipe_2',
            ingredients = 'ing-3, ing-4',
            cooking_time = 30,
            method = 'Test method 2'
        )

    
    def test_recipes_view_status_code(self):
        response = self.client.get(reverse('recipes'))
        self.assertEqual(response.status_code, 200)
    
    def test_recipes_view_template(self):
        response = self.client.get(reverse('recipes'))
        self.assertTemplateUsed(response, 'recipe/recipes.html')

    def test_recipes_view_content(self):
        response = self.client.get(reverse('recipes'))
        self.assertContains(response, 'Recipe_1')
        self.assertContains(response, 'Recipe_2')

class RecipeDetailView(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username = 'Roberto',
            password = 'ciaobellaitalia2025'
        )
        self.client.login(username="Roberto", password="ciaobellaitalia2025")


        self.recipe = Recipe.objects.create(
            name = 'Recipe_1',
            ingredients = 'ing-1, ing-2',
            cooking_time = 20,
            method = 'Test method 1',
        )

        self.recipe.liked_by.add(self.user)

    def test_recipe_detail_status_code(self):
        response = self.client.get(reverse('recipe_details', args=[self.recipe.id]))
        self.assertEqual(response.status_code, 200)
    
    def test_recipes_view_template(self):
        response = self.client.get(reverse('recipe_details',args=[self.recipe.id] ))
        self.assertTemplateUsed(response, 'recipe/recipe_details.html')

    def test_recipes_view_content(self):
        response = self.client.get(reverse('recipe_details', args=[self.recipe.id]))
        self.assertContains(response, 'Recipe_1')   

    def test_recipes_view_like(self):
        self.assertTrue(self.recipe.liked_by.filter(id = self.user.id).exists()) 
     
class RecipeSearchView(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username = 'Roberto',
            password = 'ciaobellaitalia2025'
        )
        self.client.login(username="Roberto", password="ciaobellaitalia2025")

        self.recipe = Recipe.objects.create(
            name = 'Recipe_1',
            ingredients = 'ing-1, ing-2',
            cooking_time = 20,
            difficulty = 'Easy',
            method = 'Test method 1',
        )
        self.recipe = Recipe.objects.create(
            name = 'Recipe_2',
            ingredients = 'ing-3, ing-4',
            cooking_time = 10,
            difficulty = 'Hard',
            method = 'Test method 2',
        )
    
    def test_recipe_search_status_code(self):
        response = self.client.get(reverse('search'))
        self.assertEqual(response.status_code, 200)
    
    def test_search_filter_by_name_returns_subset(self):
        response = self.client.get(reverse('search'), {'ingredients': 'ing-1'})
        self.assertContains(response, 'Recipe_1')
    
    def test_search_context_contains_charts_when_results_exist(self):
        response = self.client.get(reverse('search'), {'ingredients': '', 'max_cooking_time': 30, 'difficulty': ''})
        self.assertEqual(response.status_code, 200)

        chart_bar = response.context.get('chart_bar')
        chart_pie = response.context.get('chart_pie')
        chart_line = response.context.get('chart_line')

        self.assertIsNotNone(chart_bar)
        self.assertIsNotNone(chart_pie)
        self.assertIsNotNone(chart_line)

        





