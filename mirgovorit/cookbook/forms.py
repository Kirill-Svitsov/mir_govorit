from django import forms


class AddProductToRecipeForm(forms.Form):
    product = forms.IntegerField(label='Выберите продукт')
    weight = forms.IntegerField(label='Введите вес')
