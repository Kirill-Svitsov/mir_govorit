from django.contrib import admin
from .models import Product, Recipe, RecipeProduct


class RecipeProductInline(admin.TabularInline):
    model = RecipeProduct
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'times_cooked')
    search_fields = ('name',)
    list_filter = ('times_cooked',)
    verbose_name = 'Продукт'
    verbose_name_plural = 'Продукты'


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    inlines = [RecipeProductInline]
    list_display = ('name',)
    search_fields = ('name',)
    verbose_name = 'Рецепт'
    verbose_name_plural = 'Рецепты'


@admin.register(RecipeProduct)
class RecipeProductAdmin(admin.ModelAdmin):
    list_display = ('recipe', 'product', 'weight')
    search_fields = ('recipe__name', 'product__name')
    list_filter = ('recipe', 'product')
    verbose_name = 'Продукт в рецепте'
    verbose_name_plural = 'Продукты в рецептах'
