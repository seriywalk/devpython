class Animals:
    def __init__(self, name="", weight=0):
        self.name = name
        self.weight = weight

    def do_voice(self):
        pass

    def do_personal_action(self):
        pass


class EggLaying(Animals):  
    def do_eggs(self):
        return "дает яйца"

    def do_personal_action(self):
        return self.do_eggs() + ", " + self.do_voice()

class Cutting(Animals):  
    def do_cut(self):
        return "дает шерсть"

    def do_personal_action(self):
        return self.do_cut() + ", " + self.do_voice()


class Milking(Animals):  
    def do_milk(self):
        return "дает молоко"

    def do_personal_action(self):
        return self.do_milk() + ", " + self.do_voice()


class Chicken(EggLaying):
    atype = "Курица"

    def do_voice(self):
        return "кудахчет"


class Goose(EggLaying):
    atype = "Гусь"

    def do_voice(self):
        return "гогочет"


class Duck(EggLaying):
    atype = "Утка"

    def do_voice(self):
        return "крякает"


class Sheep(Cutting, Milking):
    atype = "Овца"

    def do_voice(self):
        return "блеет"

    def do_personal_action(self):
        return self.do_cut() + " и " + self.do_milk() + ", " + self.do_voice()


class Cow(Milking):
    atype = "Корова"

    def do_voice(self):
        return "мычит"


class Goat(Milking, Cutting):
    atype = "Коза"

    def do_voice(self):
        return "мекает"

    def do_personal_action(self):
        return self.do_cut() + " и " + self.do_milk() + ", " + self.do_voice()


# У каждого животного должно быть определено имя(self.name) и вес(self.weight).

farm = [
    Goose("Белый", 5),
    Goose("Серый", 6),
    Cow("Лепешка", 750),
    Sheep("Шон", 45),
    Sheep("Долли", 60),
    Chicken("Ко-ко", 6),
    Chicken("Кукареку", 7),
    Goat("Дереза", 35),
    Goat("Копытце", 70),
    Duck("Кряква", 3),
]

max_weight = sum_weight = 0
for animal in farm:
    print(
        f'{animal.atype} по кличке {animal.name} весит {animal.weight} кг. {animal.do_personal_action()}'
    )
    sum_weight += animal.weight
    if animal.weight > max_weight:
        max_weight = animal.weight
        atype = animal.atype
        aname = animal.name
# посчитать общий вес всех животных
print()
print(f"Вес всех животных = {sum_weight}")
# Вывести название самого тяжелого животного.
print(f"Самое тяжелое животное - это {atype} по кличке {aname} с весом = {max_weight} кг.")