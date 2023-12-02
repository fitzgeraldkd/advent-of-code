from unittest.mock import ANY

from solutions import BaseTestCase
from solutions.year_2020.day_07.solution import Year2020Day07


class TestSolution(BaseTestCase):
    def setUp(self):
        self.solution = Year2020Day07()
        self.answers = (268, 7867)


class TestSample1(BaseTestCase):
    def setUp(self):
        self.solution = Year2020Day07("sample1.txt")
        self.answers = (4, 32)


class TestSample2(BaseTestCase):
    def setUp(self):
        self.solution = Year2020Day07("sample2.txt")
        self.answers = (ANY, 126)
