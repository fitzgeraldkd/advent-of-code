from unittest.mock import ANY

from solutions import BaseTestCase
from solutions.year_2016.day_22.solution import Year2016Day22


class TestSolution(BaseTestCase):
    def setUp(self):
        self.solution = Year2016Day22()
        self.answers = (981, 233)


class TestSample(BaseTestCase):
    def setUp(self):
        self.solution = Year2016Day22("sample.txt")
        self.answers = (ANY, 7)
