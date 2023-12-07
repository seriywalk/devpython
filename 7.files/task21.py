import os

# ввод информации
dishes_lst = input("Введите список блюд из cook_book через запятую: ")
dishes_list = dishes_lst.split()

pers_count = input("Введите количество персон для кого мы будем готовить: ")
int_p_count = int(pers_count)

# формирование словаря
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
        
# поиск ингредиентов и подсчет        
shop_list = []
for d in dishes_list:
    shop_list.append(cook_book[d])

print(shop_list)
    
    