from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Recipe, Product, RecipeProduct


def main(request):
    return render(request, 'cookbook/main.html')


def recipes(request):
    recipes = Recipe.objects.all()
    context = {'recipes': recipes}
    return render(request, 'cookbook/recipes.html', context)


def add_product_to_recipe(request, recipe_id, product_id, weight):
    """Функция добавления продукта в рецепт"""
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    product = get_object_or_404(Product, pk=product_id)
    # Пытаемся получить существующий продукт в рецепте
    recipe_product, created = RecipeProduct.objects.get_or_create(
        recipe=recipe,
        product=product
    )
    if not created:
        # Если продукт уже был в рецепте, обновляем вес
        old_weight = recipe_product.weight
        recipe_product.weight = old_weight + weight
        recipe_product.save()
    else:
        # Если продукта не было в рецепте, добавляем его
        # и увеличиваем счетчик использования
        recipe.recipeproduct_set.create(product=product, weight=weight)
        product.times_cooked += 1
        product.save()
    return HttpResponse(
        f'Продукт {product.name} добавлен к рецепту {recipe.name} с весом {weight}г.'
    )


def cook_recipe(request, recipe_id):
    """
     Функция увеличивает на единицу количество приготовленных
     блюд для каждого продукта, входящего в указанный рецепт.
     """
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    # Увеличиваем количество приготовленных блюд
    # для каждого продукта в рецепте
    for recipe_product in recipe.recipeproduct_set.all():
        recipe_product.product.times_cooked += 1
        recipe_product.product.save()

    return HttpResponse(
        f'Количество приготовленных блюд для рецепта {recipe.name} увеличено.'
    )


def show_recipes_without_product(request, product_id):
    """
    Функция возвращает HTML страницу, на которой размещена таблица.
    В таблице отображены id и названия всех рецептов, в которых
    указанный продукт отсутствует, или присутствует в количестве меньше 10 грамм.
    """
    product = get_object_or_404(Product, pk=product_id)
    # Находим рецепты, где указанный продукт отсутствует или
    # присутствует в количестве меньше 10 грамм
    recipes = Recipe.objects.exclude(
        recipeproduct__product=product
    ).exclude(recipeproduct__product=product, recipeproduct__weight__gte=10)
    context = {'recipes': recipes}
    return render(request, 'recipes_without_product.html', context)
