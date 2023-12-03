from unittest import TestCase

from solutions import BaseTestCase
from solutions.year_2015.day_10.solution import Year2015Day10


class TestSolution(BaseTestCase):
    def setUp(self):
        self.solution = Year2015Day10()
        self.answers = (329356, 4666278)


class TestUtils(TestCase):
    def test_look_and_say(self):
        solution = Year2015Day10()
        self.assertEqual(solution.look_and_say('1'), '11')
        self.assertEqual(solution.look_and_say('11'), '21')
        self.assertEqual(solution.look_and_say('21'), '1211')
        self.assertEqual(solution.look_and_say('1211'), '111221')
        self.assertEqual(solution.look_and_say('111221'), '312211')
