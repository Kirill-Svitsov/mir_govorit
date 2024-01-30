[![GitHub](https://img.shields.io/badge/GitHub-Kirill--Svitsov-blue)](https://github.com/Kirill-Svitsov)
# Mir Govorit

## Description
Тестовое задание для Mir Govorit.
Нужно разработать небольшое приложение поварской книги на Django, со следующим функционалом:

 

### База данных:

В базе данных приложения храниться список продуктов. Продукт имеет название, а также целочисленное поле, хранящее информацию о том, сколько раз было приготовлено блюдо с использованием этого продукта. Также в базе данных хранятся рецепты блюд. Рецепт имеет название, а также набор входящих в рецепт продуктов, с указанием веса в граммах.

Один и тот же продукт, может использоваться в разных рецептах. Один и тот же продукт не может быть использован в одном рецепте дважды.

 

### Функционал
Приложение предоставляет следующие HTTP функции, получающие параметры методом GET

1) add_product_to_recipe с параметрами recipe_id, product_id, weight. Функция добавляет к указанному рецепту указанный продукт с указанным весом. Если в рецепте уже есть такой продукт, то функция должна поменять его вес в этом рецепте на указанный.

2) cook_recipe c параметром recipe_id. Функция увеличивает на единицу количество приготовленных блюд для каждого продукта, входящего в указанный рецепт.

3) show_recipes_without_product с параметром product_id. Функция возвращает HTML страницу, на которой размещена таблица. В таблице отображены id и названия всех рецептов, в которых указанный продукт отсутствует, или присутствует в количестве меньше 10 грамм. Страница должна генерироваться с использованием Django templates. Качество HTML верстки не оценивается.

### Реализация
Проект реализован согласно паттерну MTV, есть достаточно удобные шаблоны для тестирования проекта.

## Technologies

- Python 3.12
- Django 4.2.9
- SQLite

## Launching the Project in Development Mode

- Создать и активировать виртуальное окружение.
```
python3 -m venv venv
source venv/bin/activate
```
- Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

В папке, содержащей manage.py, выполнить команды:
```
python manage.py makemigrations
```
```
python manage.py migrate
```
Также для мануального тестирования предоставлены фикстуры. Для заполнения БД выполните следующие команды:
```
python3 manage.py loaddata fixtures/cookbook/product.json
```
```
python3 manage.py loaddata fixtures/cookbook/recipe.json
```
```
python3 manage.py loaddata fixtures/cookbook/recipeproduct.json
```
После этого можно запускать сервер:
```
python manage.py runserver
```
