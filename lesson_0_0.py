#Практическое задание по уроку "Базовые структуры данных"
# 1st program

print (9**0.5*5)

# 2nd program

print (9.99 > 9.98 and 1000 != 1000.1)

# 3rd program

print (2*2+2)
print (2*(2+2))
print ((2*2+2) == (2*(2+2)))

# 4th program

print (int(123.456*10)-(int(123.456*10)//10)*10)
#-------------------------------------------------
my_dict = {'Ivan': 1972, 'Yuriy': 1962, 'Anatoliy': 1952, 'Serg': 1968}
print('Dict:', my_dict)
print('Existing value:', my_dict['Ivan'])
print('Not existing value:', my_dict.get('Alex'))
my_dict.update({'Alex': 2007,
                'Maxim': 2006})
print(my_dict)
print('Deleted value:', my_dict['Ivan'])
del my_dict['Ivan']
print('Modified dictionary:', my_dict)
my_set = {7, 7, 7, 7, 7, 7, 7, 7, 3.14159, 3.14159, 'Pi', 'Pi', 'Pi', 'Pi'}
print('Set:', my_set)
my_set.remove(7)
my_set.add((5, 6, 1.2345))
my_set.add(8)
print('Modified set:', my_set)
#-----------------------------------------
#урок 1_3
name = "Yuriy"
print("Name:", name)
age = 61
print("Age:", age)
age = age + 1
print("New Age:", age)
is_student = True
print("is student:", is_student)
#-------------------------------------------
#урок 1_4
my_dict = {'Ivan': 1972, 'Yuriy': 1962, 'Anatoliy': 1952, 'Serg': 1968}
print('Dict:', my_dict)
print('Existing value:', my_dict['Ivan'])
print('Not existing value:', my_dict.get('Alex'))
my_dict.update({'Alex': 2007,
                'Maxim': 2006})
print(my_dict)
print('Deleted value:', my_dict['Ivan'])
del my_dict['Ivan']
print('Modified dictionary:', my_dict)
my_set = {7, 7, 7, 7, 7, 7, 7, 7, 3.14159, 3.14159, 'Pi', 'Pi', 'Pi', 'Pi'}
print('Set:', my_set)
my_set.remove(7)
my_set.add((5, 6, 1.2345))
my_set.add(8)
print('Modified set:', my_set)
#-----------------------------------------------
print('Урок 1_5')
task_count = 12
hour_count = 1.5
course_name = "Python"
task_time = hour_count / task_count
print("Курс:", course_name, ", всего задач:", task_count, ", затрачено часов:", hour_count,
      ", среднее время выполнения", task_time, "часа")
#-----------------------------------------------
print('Урок 1_6')
example = 'Топинамбур'
print(example[0])
print(example[-1])
print(example[5:])
print(example[::-1])
print(example[1::2])
#---------------------------------------------
print('Урок 1_7')
my_string = input()
print(len(my_string))
print(my_string.upper())
print(my_string.lower())
print(my_string.replace(" ", ""))
print(my_string[0])
print(my_string[-1])
#--------------------------------------------
print('Урок 1_8')
immutable_var = (1, 2, 3, 4, "a", "b")
print(immutable_var)
#immutable_var[0] = 111
#TypeError: 'tuple' object does not support item assignment
print(immutable_var)
mutable_list = [1, 2, 3, 4, "a", "b"]
print(mutable_list)
mutable_list[-1] = 'Modified'
mutable_list[0] = 11
print(mutable_list)
#--------------------------------------------
print('Урок 1_9')
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
sorted_students = sorted(students)
dict_students = dict()
students_1 = sorted_students[0]
students_2 = sorted_students[1]
students_3 = sorted_students[2]
students_4 = sorted_students[3]
students_5 = sorted_students[4]
rating_average_1 = sum(grades[0]) / len(grades[0])
rating_average_2 = sum(grades[1]) / len(grades[1])
rating_average_3 = sum(grades[2]) / len(grades[2])
rating_average_4 = sum(grades[3]) / len(grades[3])
rating_average_5 = sum(grades[4]) / len(grades[4])
dict_students = {
    students_1: rating_average_1,
    students_2: rating_average_2,
    students_3: rating_average_3,
    students_4: rating_average_4,
    students_5: rating_average_5
}
print(dict_students)
#---------------------------------------------
print('Урок 1_10')
first = input('Введите первое число : ')
second = input('Введите второе число : ')
third = input('Введите третье число : ')
if first == second and second == third:
    print(3)
elif first == second and not (second == third):
    print(2)
elif not (first == second) and second == third:
    print(2)
elif first == third and not (second == third):
    print(2)
else:
    print(0)
  #---------------------------------------------
print('Урок 1_11')
my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
my_index = 0
while my_index < len(my_list):
    if my_list[my_index] < 0:
        break
    elif my_list[my_index] == 0:
        my_index = my_index + 1
        continue
    else:
        print(my_list[my_index])
        my_index = my_index + 1
#----------------------------------------------------
print('Урок 1_12')
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
primes = []
not_primes = []
for i in numbers:
    number_of_divisors = 0
    for j in numbers:
        if i % j == 0:
            number_of_divisors = number_of_divisors + 1
    if number_of_divisors == 2:
        primes.append(numbers[i - 1])
    if number_of_divisors > 2:
        not_primes.append(numbers[i - 1])
print('numbers:', numbers)
print('Primes:', primes)
print('Not_primes:', not_primes)
#--------------------------------------------------
print('Урок 1_13')
def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        row = []
        for j in range(m):
            row.append(value)
        matrix.append(row)
    return matrix


result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)

print(result1)
print(result2)
print(result3)
#--------------------------------------------
print('Урок 1_14')
def get_password(number):
    password = ''
    for i in range(1, number):
        for j in range(2, number):
            if j <= i:
                continue
            if number % (i + j) == 0:
                password += str(i) + str(j)
    return password


n = int(input('Введите целое число от 3 до 20: '))

result = get_password(n)
print('Пароль:', result)
#-------------------------------------------------
print('Урок 1_15')
calls = 0


def count_calls():
    global calls
    calls = calls + 1


def string_info(string):
    count_calls()
    return (len(string), string.upper(), string.lower())


def is_contains(string, list_to_search):
    count_calls()
    return string.upper() in [s.upper() for s in list_to_search]


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycle', 'cyclic']))
print(calls)
