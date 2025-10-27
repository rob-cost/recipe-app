from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.auth.models import User


class Recipe (models.Model):

    name = models.CharField(max_length=255, blank=False, help_text="Enter the name of the recipe")
    ingredients = models.TextField(help_text="Insert ingredients separated by a comma")
    cooking_time = models.PositiveIntegerField(validators=[MinValueValidator(1)], help_text="Insert the cooking time in minutes")
    difficulty = models.CharField(max_length=30, editable=False)
    method = models.TextField(help_text="Describe the cooking method of the recipe")
    pic = models.ImageField(upload_to='recipes', default='no_picture.jpg')
    liked_by = models.ManyToManyField(User, related_name='liked_recipe', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def calculateDifficulty(self):
        items = [i.strip() for i in self.ingredients.split(",") if i.strip()]
        if self.cooking_time < 10 and len(items) < 4:
            return  "Easy"
        elif self.cooking_time < 10 and len(items) >= 4:
            return  "Medium"
        elif self.cooking_time >= 10 and len(items) < 4:
            return  "Intermediate"
        else:
            return "Hard"
       
    def save(self, *args, **kwargs):
        self.full_clean() 
        self.difficulty = self.calculateDifficulty()
        super().save(*args, **kwargs)
        
    def __str__(self):
        return str(self.name)