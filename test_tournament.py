# import unittest
#
# class Runner:
#     def __init__(self, name, speed):
#         self.name = name
#         self.speed = speed
#
# class Tournament:
#     def __init__(self, distance):
#         self.distance = distance
#
#     def start(self, runners):
#         # Логическая ошибка: бегуны с меньшей скоростью могут пробежать дистанцию быстрее
#         # Исправленный вариант:
#         results = sorted(runners, key=lambda runner: self.distance / runner.speed)
#         return {i + 1: runner.name for i, runner in enumerate(results)}
#
# class TournamentTest(unittest.TestCase):
#     @classmethod
#     def setUpClass(cls):
#         cls.all_results = {}
#
#     def setUp(self):
#         self.usain = Runner("Усэйн", 10)
#         self.andrey = Runner("Андрей", 9)
#         self.nik = Runner("Ник", 3)
#
#     @classmethod
#     def tearDownClass(cls):
#         for key in sorted(cls.all_results.keys()):
#             print(cls.all_results[key])
#
#     def test_race_usain_and_nik(self):
#         tournament = Tournament(90)
#         runners = [self.usain, self.nik]
#         result = tournament.start(runners)
#         self.all_results[len(self.all_results) + 1] = result
#         self.assertTrue(result[max(result.keys())] == "Ник")
#
#     def test_race_andrey_and_nik(self):
#         tournament = Tournament(90)
#         runners = [self.andrey, self.nik]
#         result = tournament.start(runners)
#         self.all_results[len(self.all_results) + 1] = result
#         self.assertTrue(result[max(result.keys())] == "Ник")
#
#     def test_race_usain_andrey_and_nik(self):
#         tournament = Tournament(90)
#         runners = [self.usain, self.andrey, self.nik]
#         result = tournament.start(runners)
#         self.all_results[len(self.all_results) + 1] = result
#         self.assertTrue(result[max(result.keys())] == "Ник")
#
# if __name__ == '__main__':
#     unittest.main()



import unittest

from runner import Runner, Tournament


class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.usain = Runner("Усэйн", 10)
        self.andrey = Runner("Андрей", 9)
        self.nik = Runner("Ник", 3)

    @classmethod
    def tearDownClass(cls):
        for key in sorted(cls.all_results.keys()):
            print(cls.all_results[key])

    def test_race_usain_and_nik(self):
        tournament = Tournament(90)
        tournament.add_runner(self.usain)
        tournament.add_runner(self.nik)
        result = tournament.start()
        self.all_results[len(self.all_results) + 1] = result
        self.assertTrue(result[max(result.keys())] == "Ник")

    def test_race_andrey_and_nik(self):
        tournament = Tournament(90)
        tournament.add_runner(self.andrey)
        tournament.add_runner(self.nik)
        result = tournament.start()
        self.all_results[len(self.all_results) + 1] = result
        self.assertTrue(result[max(result.keys())] == "Ник")

    def test_race_usain_andrey_and_nik(self):
        tournament = Tournament(90)
        tournament.add_runner(self.usain)
        tournament.add_runner(self.andrey)
        tournament.add_runner(self.nik)
        result = tournament.start()
        self.all_results[len(self.all_results) + 1] = result
        self.assertTrue(result[max(result.keys())] == "Ник")

if __name__ == '__main__':
    unittest.main()
