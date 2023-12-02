from unittest.mock import ANY

from solutions import BaseTestCase
from solutions.year_2018.day_02.solution import Year2018Day02


class TestSolution(BaseTestCase):
    def setUp(self):
        self.solution = Year2018Day02()
        self.answers = (7221, "mkcdflathzwsvjxrevymbdpoq")


class TestSample1(BaseTestCase):
    def setUp(self):
        self.solution = Year2018Day02("sample_1.txt")
        self.answers = (12, ANY)


class TestSample2(BaseTestCase):
    def setUp(self):
        self.solution = Year2018Day02("sample_2.txt")
        self.answers = (ANY, "fgij")
