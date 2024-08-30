
my_string = input()
print(my_string.__len__())
print(my_string.upper())
print(my_string.lower())


my_string = my_string.split()
my_string = ''.join(my_string)
print(my_string)
print(my_string.__len__())

print(my_string[:1])
ln = my_string.__len__()
print(my_string[ln -1:])
