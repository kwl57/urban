

immutable_var = (1,2,3,4,['s','t','r','i','n','g'], True)
print(immutable_var)
print('можно менять содержимое элемента кордеджа')
immutable_var[4][1] = 'T'
print(immutable_var)

print(immutable_var[4][1])

print('сам элемент кортеджа изменить нельзя')
#immutable_var[4] = ['S','T','R','I','N','G']
print(immutable_var)

print("Изменяемый список: mutable_list = [1, 2, 3, 4, 'string']")
mutable_list = [1, 2, 3, 4, 'string']
print(mutable_list)
mutable_list[2] = 30
print(mutable_list)