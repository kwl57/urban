# module_5_2.py  Домашняя работа по уроку "Специальные методы классов"
#Необходимо дополнить класс House следующими специальными методами:
#__len__(self) - должен возвращать кол-во этажей здания self.number_of_floors.
#__str__(self) - должен возвращать строку: "Название: <название>, кол-во этажей: <этажи>".


class House:
    def __init__(self, name, number_of_floor):
        self.name = name
        self.number_of_floor = number_of_floor

    def go_to(self, new_floor):
        if 1 <= new_floor <= self.number_of_floor:
            for i in range(new_floor):
                i += 1
                print(i)
        else:
            print("Такого этажа не существует")

    def __len__(self):
        return self.number_of_floor

    def __str__(self):
        return f'Название {self.name}, кол-во этажей: {self.number_of_floor}'


h1 = House('ЖК Ягодное', 10)
h2 = House('ЖК Мечта', 20)
print(h1)
print(h2)
print(len(h1))
print(len(h2))
