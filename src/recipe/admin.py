from django.contrib import admin
from .models import Recipe

@admin.register(Recipe)

class RecipeAdmin(admin.ModelAdmin):
    list_display = ['name', 'cooking_time', 'difficulty', 'pic']
    readonly_fields = ['difficulty']