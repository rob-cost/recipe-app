from django.test import TestCase
from django.core.exceptions import ValidationError
from .models import Recipe

class RecipeModelTest(TestCase):

    def test_name_cannot_be_empty(self):
        recipe = Recipe(name="", ingredients="flour, sugar", cooking_time=5, method="Test")
        with self.assertRaises(ValidationError):
            recipe.full_clean()  # triggers clean() and field validations

    def test_ingredients_must_be_comma_separated(self):
        recipe = Recipe(name="Cake", ingredients="  ", cooking_time=5, method="Test")
        with self.assertRaises(ValidationError):
            recipe.full_clean()

    def test_cooking_time_must_be_positive(self):
        recipe = Recipe(name="Cake", ingredients="flour, sugar", cooking_time=0, method="Test")
        with self.assertRaises(ValidationError):
            recipe.full_clean()

    def test_difficulty_calculation_easy(self):
        recipe = Recipe(name="Salad", ingredients="lettuce, tomato", cooking_time=5, method="Test")
        recipe.full_clean()
        self.assertEqual(recipe.difficulty, "Easy")

    def test_difficulty_calculation_medium(self):
        recipe = Recipe(name="Soup", ingredients="water, carrot, potato, onion", cooking_time=5, method="Test")
        recipe.full_clean()
        self.assertEqual(recipe.difficulty, "Medium")

    def test_difficulty_calculation_intermediate(self):
        recipe = Recipe(name="Steak", ingredients="beef, salt", cooking_time=15, method="Test")
        recipe.full_clean()
        self.assertEqual(recipe.difficulty, "Intermediate")

    def test_difficulty_calculation_hard(self):
        recipe = Recipe(name="Lasagna", ingredients="pasta, cheese, tomato, beef", cooking_time=15, method="Test")
        recipe.full_clean()
        self.assertEqual(recipe.difficulty, "Hard")

