from django.urls import path
from cookbook import views

app_name = 'cookbook'

urlpatterns = [
    path('', views.main, name='main'),
    path('recipes/', views.recipes, name='recipes'),
    path('recipe_detail/<int:recipe_id>', views.recipe_detail, name='recipe_detail'),
    path('products/', views.products, name='products'),
    path('product_detail/<int:product_id>/', views.product_detail, name='product_detail'),
    path(
        'add_product_to_recipe/<int:recipe_id>/',
        views.add_product_to_recipe,
        name='add_product_to_recipe'
    ),
    path(
        'show_recipes_without_product/<int:product_id>/',
        views.show_recipes_without_product,
        name='show_recipes_without_product'
    ),
    path('cook_recipe/<int:recipe_id>/', views.cook_recipe, name='cook_recipe'),
]
