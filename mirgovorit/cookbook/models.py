from django.db import models


class Product(models.Model):
    """Модель продукта"""
    name = models.CharField(
        max_length=255,
        unique=True,
        verbose_name='Название продукта'
    )
    times_cooked = models.PositiveIntegerField(
        default=0,
        verbose_name='Количество использований'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class Recipe(models.Model):
    """Модель рецепта"""
    name = models.CharField(
        max_length=255,
        verbose_name='Название рецепта'
    )
    products = models.ManyToManyField(
        Product,
        through='RecipeProduct',
        verbose_name='Продукты в рецепте',
        related_name='recipes'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'


class RecipeProduct(models.Model):
    """Промежуточная модель для связи продуктов с рецептами."""
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        verbose_name='Рецепт'
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        verbose_name='Продукт'
    )
    weight = models.PositiveSmallIntegerField(verbose_name='Вес продукта в рецепте')

    def __str__(self):
        return f"{self.product} ({self.weight}г)"

    class Meta:
        verbose_name = 'Продукт в рецепте'
        verbose_name_plural = 'Продукты в рецептах'
