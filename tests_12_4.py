'''
Задача "Логирование бегунов":
В первую очередь скачайте исходный код, который нужно обложить тестами с GitHub. (Можно скопировать)
Основное обновление - выбрасывание исключений, если передан неверный тип в name и
если передано отрицательное значение в speed.
'''
import logging
import unittest
import rt_with_exceptions as runner

'''
Для решения этой задачи вам понадобиться класс RunnerTest из предыдущей задачи.
В модуле tests_12_4.py импортируйте пакет logging и настройте basicConfig на следующие параметры:
Уровень - INFO
Режим - запись с заменой('w')
Название файла - runner_tests.log
Кодировка - UTF-8
Формат вывода - на своё усмотрение, обязательная информация: уровень логирования, сообщение логирования.
'''
class RunnerTest(unittest.TestCase):
    is_frozen = False

    @classmethod
    def setUpClass(cls):
        logging.basicConfig(filename='runner_tests.log', filemode='w', level=logging.INFO, encoding='utf-8',
                            format='%(asctime)s | %(levelname)s | %(message)s')

    '''    Дополните методы тестирования в классе RunnerTest следующим образом:
    test_walk:
    Оберните основной код конструкцией try-except.
    При создании объекта Runner передавайте отрицательное значение в speed.
    В блок try добавьте логирование INFO с сообщением '"test_walk" выполнен успешно'
    В блоке except обработайте исключение соответствующего типа и логируйте его на уровне WARNING
    с сообщением "Неверная скорость для Runner".'''

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        '''
        test_walk - метод, в котором создаётся объект класса Runner с произвольным именем.
        Далее вызовите метод walk у этого объекта 10 раз.
        После чего методом assertEqual сравните distance этого объекта со значением 50.
        '''
        try:
            rn = runner.Runner(name='Бегунъ', speed=-100)
            for _ in range(10):
                rn.walk()
            self.assertEqual(rn.distance, 50)
        except ValueError:
            logging.warning(msg='Неверная скорость для Runner')  #, exc_info=True)
        logging.info('Тест "test_walk" выполнен успешно')

    '''
    test_run:
    Оберните основной код конструкцией try-except.
    При создании объекта Runner передавайте что-то кроме строки в name.
    В блок try добавьте логирование INFO с сообщением '"test_run" выполнен успешно'
    В блоке except обработайте исключение соответствующего типа и логируйте его на уровне WARNING 
    с сообщением "Неверный тип данных для объекта Runner".
    '''
    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        '''
        test_run - метод, в котором создаётся объект класса Runner с произвольным именем.
        Далее вызовите метод run у этого объекта 10 раз.
        После чего методом assertEqual сравните distance этого объекта со значением 100.
        '''
        try:
            rn = runner.Runner(name=7, speed=7)
            for _ in range(10):
                rn.run()
            self.assertEqual(rn.distance, 100)
        except TypeError:
            logging.warning('Неверный тип данных для объекта Runner')  #, exc_info=True)
        logging.info('Тест "test_run" выполнен успешно')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        '''
        test_challenge - метод в котором создаются 2 объекта класса Runner с произвольными именами.
        Далее 10 раз у объектов вызываются методы run и walk соответственно.
        Т.к. дистанции должны быть разными, используйте метод assertNotEqual, чтобы убедится в неравенстве результатов.
        '''
        rna = runner.Runner(name='RNA') # РНК :-)
        rnb = runner.Runner(name='RnB') # R'n'B :)
        for _ in range(10):
            rna.run()
            rnb.walk()
        self.assertNotEqual(rna.distance, rnb.distance)

if __name__ == '__main__':
    # logging.basicConfig(filename='runner_tests.log', filemode='w', level=logging.INFO, encoding='utf-8',
    #                     format='%(asctime)s | %(levelname)s | %(message)s')
    # -- перенес в setUpClass(cls)!
    unittest.main()
