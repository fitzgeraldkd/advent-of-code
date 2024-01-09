from unittest.mock import ANY

from solutions import BaseTestCase
from solutions.year_2016.day_15.solution import Year2016Day15


class TestSolution(BaseTestCase):
    def setUp(self):
        self.solution = Year2016Day15()
        self.answers = (148737, 2353212)


class TestSample(BaseTestCase):
    def setUp(self):
        self.solution = Year2016Day15("sample.txt")
        self.answers = (5, ANY)
