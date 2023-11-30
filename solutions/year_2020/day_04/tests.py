from unittest.mock import ANY

from solutions import BaseTestCase
from solutions.year_2020.day_04.solution import Year2020Day04


class TestSolution(BaseTestCase):
    def setUp(self):
        self.solution = Year2020Day04(__file__)
        self.answers = (216, 150)


class TestSample1(BaseTestCase):
    def setUp(self):
        self.solution = Year2020Day04(__file__, "sample1.txt")
        self.answers = (2, ANY)


class TestSample2(BaseTestCase):
    def setUp(self):
        self.solution = Year2020Day04(__file__, "sample2.txt")
        self.answers = (ANY, 4)
