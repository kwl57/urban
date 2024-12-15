import unittest
from test_12_2 import Runner, Tournament

class RunnerTest(unittest.TestCase):
    is_frozen = True

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены'.")
    def test_walk(self):
        runner = Runner("Тестовый бегун")
        for i in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены'.")
    def test_run(self):
        runner = Runner("Тестовый бегун")
        for i in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены'.")
    def test_challenge(self):
        runner1 = Runner("Тестовый бегун1")
        runner2 = Runner("Тестовый бегун2")
        for i in range(10):
            runner1.run()
            runner2.walk()
        self.assertNotEqual(runner1.distance, runner2.distance)

class TournamentTest(unittest.TestCase):
    is_frozen = 0

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner1 = Runner("Усэйн", speed = 10)
        self.runner2 = Runner("Андрей", speed = 9)
        self.runner3 = Runner("Ник", speed = 3)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены'.")
    def test_usain_nick(self):
        tournament = Tournament(90, self.runner1, self.runner3)
        results = tournament.start()
        self.all_results[len(self.all_results)+1] = results
        self.assertTrue(results[max(results.keys())] == "Ник")

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены'.")
    def test_andrey_nick(self):
        tournament = Tournament(90, self.runner2, self.runner3)
        results = tournament.start()
        self.all_results[len(self.all_results)+1] = results
        self.assertTrue(results[max(results.keys())] == "Ник")

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены'.")
    def test_usain_andrey_nick(self):
        tournament = Tournament(90, self.runner1, self.runner2, self.runner3)
        results = tournament.start()
        self.all_results[len(self.all_results)+1] = results
        self.assertTrue(results[max(results.keys())] == "Ник")