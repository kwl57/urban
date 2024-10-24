from os import walk
from os.path import join, getmtime, getsize, dirname
from time import strftime, localtime

#Используйте os.walk для обхода каталога, путь к которому указывает переменная directory
#Примените os.path.join для формирования полного пути к файлам.
#Используйте os.path.getmtime и модуль time для получения и отображения времени последнего изменения файла.
#Используйте os.path.getsize для получения размера файла.
#Используйте os.path.dirname для получения родительской директории файла.

def show_path_info(directory):
    '''выводит информацию о всех файлах в указанной директории'''
    for root, dirs, files in walk(directory):
        for file in files:
            filepath = join(root, file)
            filetime = getmtime(filepath)
            formatted_time = strftime("%d.%m.%Y %H:%M", localtime(filetime))
            filesize = getsize(filepath)
            parent_dir = dirname(filepath)
            # parent_dir = root  # то же самое
            print(f'Обнаружен файл: {file},',
                  f'Путь: {filepath},',
                  f'Размер: {filesize} байт,',
                  f'Время изменения: {formatted_time},',
                  f'Родительская директория: {parent_dir}')


if __name__ == '__main__':
    show_path_info('.')