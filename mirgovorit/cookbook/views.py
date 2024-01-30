from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse

from .models import Recipe, Product, RecipeProduct
from .forms import AddProductToRecipeForm


def main(request):
    recipes = Recipe.objects.all()
    context = {
        'recipes': recipes
    }
    return render(request, 'cookbook/main.html', context)


def recipes(request):
    recipes = Recipe.objects.prefetch_related('recipeproduct_set__product').all()
    products = Product.objects.all()
    context = {
        'recipes': recipes,
        'products': products
    }
    return render(request, 'cookbook/recipes.html', context)


def recipe_detail(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    products = Product.objects.all()
    context = {
        'recipe': recipe,
        'products': products
    }
    return render(request, 'cookbook/recipe_detail.html', context)


def products(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'cookbook/products.html', context)


def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    recipes = Recipe.objects.all()
    context = {
        'recipes': recipes,
        'product': product
    }
    return render(request, 'cookbook/product_detail.html', context)


def add_product_to_recipe(request, recipe_id):
    """Функция добавления продукта в рецепт"""
    if request.method == 'POST':
        product_id = request.POST.get('product')
        weight = request.POST.get('weight')

        recipe = get_object_or_404(Recipe, pk=recipe_id)
        product = get_object_or_404(Product, pk=product_id)

        try:
            # Пытаемся получить существующий продукт в рецепте
            recipe_product = RecipeProduct.objects.get(recipe=recipe, product=product)
            # Если продукт уже был в рецепте, обновляем вес
            recipe_product.weight += int(weight)
            recipe_product.save()
        except RecipeProduct.DoesNotExist:
            # Если продукта не было в рецепте, добавляем его
            # и увеличиваем счетчик использования
            recipe_product = RecipeProduct.objects.create(recipe=recipe, product=product, weight=int(weight))
            product.times_cooked += 1
            product.save()

        return HttpResponse(
            f'Продукт {product.name} добавлен к рецепту {recipe.name} с весом {weight}г.'
        )
    else:
        # Обработка случая, когда запрос не является POST
        # Может потребоваться другая логика или редирект
        return HttpResponse('Метод запроса не поддерживается')


def show_recipes_without_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    # Находим рецепты, где указанный продукт отсутствует
    # или присутствует в количестве менее 10 грамм
    recipes = Recipe.objects.exclude(
        recipeproduct__product=product,
        recipeproduct__weight__gte=10
    )
    context = {
        'recipes': recipes,
        'product': product
    }
    return render(request, 'cookbook/recipes_without_product.html', context)


def cook_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)

    # Увеличиваем количество times_cooked для каждого продукта в рецепте
    for recipe_product in recipe.recipeproduct_set.all():
        recipe_product.product.times_cooked += 1
        recipe_product.product.save()

    return redirect('cookbook:recipe_detail', recipe_id=recipe.id)
