from django.urls import path
from cookbook import views

app_name = 'cookbook'

urlpatterns = [
    path('', views.main, name='main'),
    path('recipes/', views.recipes, name='recipes'),
    path(
        'add_product_to_recipe/<int:recipe_id>/<int:product_id>/<int:weight>/',
        views.add_product_to_recipe,
        name='add_product_to_recipe'
    ),
    path('cook_recipe/<int:recipe_id>/', views.cook_recipe, name='cook_recipe'),
    path(
        'show_recipes_without_product/<int:product_id>/',
        views.show_recipes_without_product,
        name='show_recipes_without_product'
    ),
]