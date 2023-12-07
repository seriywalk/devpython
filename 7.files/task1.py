import os

path = os.path.join(os.getcwd(), 'recipes.txt')
with open(path) as recipe_file:
    cook_book = {}  # книга рецептов - словарь
    for string in recipe_file:
        dish = string.strip()  # название блюда
        ingredients_count = int(recipe_file.readline().strip())  # количество ингредиентов
        dish_list = []  # список ингредиентов
        for item in range(ingredients_count):
            #  ингредиенты
            ingredient_name, quantity, measure = recipe_file.readline().strip().split('|')
            #  Добавить ингредиент
            dish_list.append({'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure})
            cook_book[dish] = dish_list  #  добавить рецепт
        recipe_file.readline()  # пустая строка

# вывод книги рецептов
    print("cook_book = {")
    for dish in cook_book:
        print(dish)
        print(ingredients_count)
        print(*dish_list, sep='\n')

