from unittest.mock import ANY

from solutions import BaseTestCase
from solutions.year_2016.day_12.solution import Year2016Day12


class TestSolution(BaseTestCase):
    def setUp(self):
        self.solution = Year2016Day12()
        self.answers = (318007, 9227661)


class TestSample(BaseTestCase):
    def setUp(self):
        self.solution = Year2016Day12("sample.txt")
        self.answers = (42, ANY)
