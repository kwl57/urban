# МИФИЧЕСКОЕ НАСЛЕДОВАНИЕ
class Horse:  #Класс описывающий лошадь

    def __init__(self):
        self.x_distance = 0  #путь
        self.sound = 'Frrr'   #звук лошади
        super().__init__()
    def run(self, dx):
        self.x_distance += dx   #увеличивает путь на dx

class Eagle:    #Класс орла

    def __init__(self):
        self.y_distance = 0  #высота
        self.sound = 'I train, eat, sleep and repeat'  #звук орла
    def fly(self, dy):   #увеличивает высоту на dy
        self.y_distance += dy

class Pegasus(Horse, Eagle):    #Класс Пегаса
    def __init__(self):
        super().__init__()

    def move(self, dx, dy):  #изменение дистанции
        super().run(dx)
        super().fly(dy)

    def get_pos(self):    #возвращает текущее положение пегаса в виде кортежа
        return self.x_distance, self.y_distance

    def voice(self):  #звук пегаса
        print(self.sound)



p1 = Pegasus()


print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()

