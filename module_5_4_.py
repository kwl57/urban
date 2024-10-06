class House:
    houses_history = []

    def __new__(cls, *args, **kwargs):
        cls.houses_history.append(args[0])
        return object.__new__(cls)

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __str__(self):
        return self.name

    def __del__(self):
        print(f'Дом в {self.name} снесён, но он останется в истории')


# Пример выполняемого кода:
h1 = House('ЖК Ягодное', 10)
print(House.houses_history)
h2 = House('ЖК Мечта', 20)
print(House.houses_history)
del h1
del h2
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)
del h3

print("Все дома снесены ")
h4 = House('ЖК Марс', 20)
print(House.houses_history)
del h4
print("Выходим  из модул  и все сносим!!! ")
