from django.urls import path
from . import views

urlpatterns =[
    path('homepage', views.homepage_view, name='homepage'),
    path('recipes', views.recipes_view, name='recipes'),
    path('recipes/<int:recipe_id>', views.recipe_details, name='recipe_details'),
    path('recipes/<int:recipe_id>/toggle_like', views.toggle_like, name='toggle_like')
]