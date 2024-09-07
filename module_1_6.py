#- Выведите на экран словарь my_dict.
#  - Выведите на экран одно значение по существующему ключу, одно по отсутствующему из словаря my_dict без ошибки.
#  - Добавьте ещё две произвольные пары того же формата в словарь my_dict.
# - Удалите одну из пар в словаре по существующему ключу из словаря my_dict и выведите значение из этой пары на экран.
#  - Выведите на экран словарь my_dict.

my_dict = {'Vova': 1957, 'Piter': 1960, 'Egor':1980}
print(my_dict)

print(my_dict['Vova'])
print(my_dict.get('Adam'))
my_dict['Eva'] = 1000
my_dict['Adam'] = 999
print(my_dict)
b = my_dict.pop('Eva')
print(b)
print(my_dict.get('Eva', 'Ева удалена из рая'))
print(my_dict.get('Adam', 'Adam удалена из рая'))
print(my_dict)

#абота с множествами:
#  - Создайте переменную my_set и присвойте ей множество, состоящее из разных типов данных с повторяющимися значениями.
#  - Выведите на экран множество my_set (должны отобразиться только уникальные значения).
#  - Добавьте 2 произвольных элемента в множество my_set, которых ещё нет.
#  - Удалите один любой элемент из множества my_set.
#  - Выведите на экран измененное множество my_set.

print('Множество')
my_set = {1,3,4,'str', 5, 8, 3,4}
print(my_set)
print(" Добавляем 'str2',9")
my_set.update({'str2',9})
print(my_set)
print(" Удаляем 9")
my_set.discard(9)
print(my_set)