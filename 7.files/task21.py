import os

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

def get_shop_list_by_dishes(dishes_lst, pers_count):        
# поиск ингредиентов к блюдам
# ввод информации
    dishes_lst = input("Введите список блюд из cook_book через запятую: ")
    dishes_list = dishes_lst.split(',')

    # dishes_list = ['Фахитос', 'Омлет']
    # print(dishes_list)
    pers_count = input("Введите количество персон для кого мы будем готовить: ")
    pers_count = '2'

    preshop_list = []
    shop_list = []
    for d in dishes_list:
        for ingredient in cook_book[d]:
            preshop_list  = dict([(ingredient['ingredient_name'],
            {'quantity': int(ingredient['quantity']) * int(pers_count),
            'measure': ingredient['measure']})])
            shop_list.append(cook_book[d])
        if preshop_list.get(ingredient['ingredient_name']) == 'None':
            sum_ingr = (int(shop_list[ingredient['ingredient_name']]['quantity']) +
                        int(preshop_list[ingredient['ingredient_name']]['quantity']))
            shop_list[ingredient['ingredient_name']]['quantity'] = sum_ingr
        else:
            shop_list.update(preshop_list)
    return shop_list 
                    
    print(shop_list)                    

    