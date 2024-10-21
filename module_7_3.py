import string
###
#"Напишите класс WordsFinder, объекты которого создаются следующим образом:
#WordsFinder('file1.txt, file2.txt', 'file3.txt', ...).
#Объект этого класса должен принимать при создании неограниченного количество названий файлов и записывать их в атрибут file_names в виде списка или кортежа.
#Также объект класса WordsFinder должен обладать следующими методами:
#get_all_words - подготовительный метод, который возвращает словарь следующего вида:
#{'file1.txt': ['word1', 'word2'], 'file2.txt': ['word3', 'word4'], 'file3.txt': ['word5', 'word6', 'word7']}
#Где:
#'file1.txt', 'file2.txt', ''file3.txt'' - названия файлов.
#['word1', 'word2'], ['word3', 'word4'], ['word5', 'word6', 'word7'] - слова содержащиеся в этом файле.
#
#test_file.txt
#It's a text for task Найти везде,
#Используйте его для самопроверки.
#Успехов в решении задачи!
#text text text
#####



class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as file:
                text = file.read().lower()
                # Убираем пунктуацию
                text = text.translate(str.maketrans('', '', string.punctuation.replace('-', '')))
                # Разбиваем на слова
                words = text.split()
                all_words[file_name] = words
        return all_words

    def find(self, word):
        results = {}
        all_words = self.get_all_words()
        for file_name, words in all_words.items():
            #if word.lower() in words:
                results[file_name] = words.index(word.lower()) + 1  # Позиция с 1
        return results

    def count(self, word):
        results = {}
        all_words = self.get_all_words()
        for file_name, word_ in all_words.items():
            count = word_.count(word.lower())
            if count > 0:
                results[file_name] = count
        return results

# test
finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())
print(finder2.find('TEXT'))
print(finder2.count('teXT'))

#{'test_file.txt': ["it's", 'a', 'text', 'for', 'task', 'найти', 'везде', 'используйте', 'его', 'для', 'самопроверки', 'успехов', 'в', 'решении', 'задачи', 'text', 'text', 'text']}
#{'test_file.txt': 3}
#{'test_file.txt': 4}

#finder1 = WordsFinder('Mother Goose - Monday’s Child.txt',)
#print(finder1.get_all_words())
#print(finder1.find('Child'))
#print(finder1.count('Child'))
#{'Mother Goose - Monday’s Child.txt': ['monday’s', 'child', 'monday’s', 'child', 'is', 'fair', 'of', 'face', 'tuesday’s', 'child', 'is', 'full', 'of', 'grace', 'wednesday’s', 'child', 'is', 'full', 'of', 'woe', 'thursday’s', 'child', 'has', 'far', 'to', 'go', 'friday’s', 'child', 'is', 'loving', 'and', 'giving', 'saturday’s', 'child', 'works', 'hard', 'for', 'a', 'living', 'and', 'the', 'child', 'that', 'is', 'born', 'on', 'the', 'sabbath', 'day', 'is', 'bonny', 'and', 'blithe', 'and', 'good', 'and', 'gay', 'mother', 'goose']}
#{'Mother Goose - Monday’s Child.txt': 2}
#{'Mother Goose - Monday’s Child.txt': 8}