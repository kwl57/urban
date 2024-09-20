

data_structure = [[1, 2, 3], {'a': 4, 'b': 5}, (6, {'cube': 7, 'drum': 8}), "Hello", ((), [{(2, 'Urban', ('Urban2', 35))}])]

def cont (data):
    cont_ = 0


    def recurse (i):
        nonlocal cont_                          # переменная из ближайшей области видимости
        if isinstance(i, (int, float)):         # проверяем на "число"
            cont_ += i                          # добавляем число к cont_
        elif isinstance(i, str):                # проверяем на "букву"
            cont_ += len(i)                     # добавляем длинну к cont_
        elif isinstance(i, (list, set, tuple)): # проверяем на "список, множество, кортеж"
            for i_ in i:
                recurse(i_)                     # рекурсия в "список, множество, кортеж"
        elif isinstance(i, dict):               # проверяем на "словарь"
            for key, value, in i.items():
                recurse(key)                    # рекурсия в "ключ словаря"
                recurse(value)                  # рекурсия в "значение словаря"


    recurse(data)                               # рекурсия функции
    return cont_                                # возвращаем значение cont_ после рекурсии


result = cont(data_structure)
print("Сумма всех чисел и длин всех строк: ", result)
