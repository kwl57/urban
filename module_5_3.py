class House:

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors  # кол-во этажей

    def go_to(self, new_floor):

            if new_floor > self.number_of_floors or new_floor <= 0:
               print("Такого этажа не существует")
            else:
                l = list(range(1, new_floor + 1))
                for i in l:
                    print(f'{i}')
    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'

    def __len__(self):
        return self.number_of_floors

    @classmethod
    def __verify_type__(cls, other):
        if not isinstance(other, (int, House)):
            raise TypeError('Неправильный тип')
        return other if isinstance(other, int) else other.number_of_floors

    def __add__(self, value):
        if not isinstance(value, (int)):
            raise ArithmeticError('Неправильный тип')

        self.number_of_floors += value
        return self

    def __radd__(self, value):
        return self + value

    def __iadd__(self, value):
        self.__add__(value)
        return self


    def __eq__(self, other):
        sc = self.__verify_type__(other)
        return self.number_of_floors == sc

    def __gt__(self, other):
        sc = self.__verify_type__(other)
        return self.number_of_floors > sc

    def __ge__(self, other):
        sc = self.__verify_type__(other)
        return self.number_of_floors >= sc

    def __lt__(self, other):
        sc = self.__verify_type__(other)
        return self.number_of_floors < sc

    def __le__(self, other):
        sc = self.__verify_type__(other)
        return self.number_of_floors <= sc

    def __ne__(self, other):
        sc = self.__verify_type__(other)
        return self.number_of_floors != sc

h1 = House('ЖК Ягодное', 10)
h2 = House('ЖК Мечта', 20)


print(h1)
print(h2)

print(h1 == h2) # __eq__

h1 = h1 + 10 # __add__
print(h1)
print(h1 == h2)

h1 += 10 # __iadd__
print(h1)

h2 = 10 + h2 # __radd__
print(h2)

print(h1 > h2) # __gt__
print(h1 >= h2) # __ge__
print(h1 < h2) # __lt__
print(h1 <= h2) # __le__
print(h1 != h2) # __ne__