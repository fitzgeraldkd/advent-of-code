from unittest.mock import ANY

from solutions import BaseTestCase
from solutions.year_2016.day_21.solution import Year2016Day21


class TestSolution(BaseTestCase):
    def setUp(self):
        self.solution = Year2016Day21()
        self.answers = ("bfheacgd", "gcehdbfa")


class TestSample(BaseTestCase):
    def setUp(self):
        self.solution = Year2016Day21("sample.txt")
        self.answers = ("decab", ANY)

    def test_part_1(self):
        self.assertEqual(self.solution.part_1("abcde"), self.answers[0])
