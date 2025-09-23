from django.db import models
from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError

class Recipe (models.Model):
    name = models.CharField(max_length=255, blank=False, help_text="Enter the name of the recipe")
    ingredients = models.TextField(help_text="Insert ingredients separated by a comma")
    cooking_time = models.PositiveIntegerField(validators=[MinValueValidator(1)], help_text="Insert the cooking time in minutes")
    difficulty = models.CharField(max_length=30, editable=False)
    method = models.TextField(help_text="Describe the cooking method of the recipe")
    likes = models.PositiveIntegerField(default=0)

    def calculateDifficulty(self):
        items = [i.strip() for i in self.ingredients.split(",") if i.strip()]
        if self.cooking_time < 10 and len(items) < 4:
            self.difficulty = "Easy"
        elif self.cooking_time < 10 and len(items) >= 4:
            self.difficulty = "Medium"
        elif self.cooking_time >= 10 and len(items) < 4:
            self.difficulty = "Intermediate"
        elif self.cooking_time >= 10 and len(items) >= 4:
            self.difficulty = "Hard"

    def clean(self):
        #make sure that name field is not empty
        if not self.name:
            raise ValidationError("Name cannot be empty")
        
        #make sure that ingredients are well formatted and not empty
        items = [i.strip() for i in self.ingredients.split(",") if i.strip()]
        if not items:
            raise ValidationError("Ingredients must be separated by a comma")
       
    def save(self, *args, **kwargs):
        self.full_clean() 
        self.calculateDifficulty()
        super().save(*args, **kwargs)
        
    def __str__(self):
        return str(self.name)