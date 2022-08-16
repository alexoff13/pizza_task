class PizzaSize:
    def __init__(self):
        self.s = 25
        self.m = 30
        self.l = 35
        self.xl = 40


class Pizza:
    def __init__(self, name: str, describe: str, size: int, count_ingredients: int):
        # ToDo добавить проверки перед присовоением полей
        self.count_ingredients = count_ingredients
        self.size = size
        self.describe = describe
        self.name = name
        self.count_cheese = 0
        self.count_salt = 0

    @property
    def price(self):
        return (self.count_ingredients * 50) * (1 + self.size / 100) + self.count_cheese * 13 + self.count_salt * 3

    def add_salt(self):
        self.count_salt += 1

    def add_cheese(self):
        self.count_cheese += 1

    def __repr__(self):
        ...
        # todo


class Order:
    def __init__(self, list_pizzas: list[Pizza]):
        # type(list_pizzas[0]) == Pizza
        # ToDo добавить проверки перед присовоением полей
        self.list_pizzas = list_pizzas

    def add_pizza(self, pizza: Pizza):
        # ToDo добавить проверки перед присовоением полей
        self.list_pizzas.append(pizza)

    def __repr__(self):
        ...
        # todo можно использовать в цикле print(pizza)
