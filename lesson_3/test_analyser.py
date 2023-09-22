import unittest

from task_5_analyser import MoodAnalyser


class TestMoodAnalyser(unittest.TestCase):
    def setUp(self) -> None:
        self.analyser = MoodAnalyser()

    def test_fun_mood(self):
        self.assertEqual(self.analyser.mood_analyser('У меня веселое настроение'), 'веселое')

    def test_sad_mod(self):
        self.assertEqual(self.analyser.mood_analyser('У меня грустное настроение'), 'грустное')

    def test_happy_mod(self):
        self.assertEqual(self.analyser.mood_analyser('У меня счастливое настроение'), 'счастливое')

    def test_without_mood(self):
        self.assertEqual(self.analyser.mood_analyser('asdf sdgfg sfdgfhg'), 'неизвестное')
