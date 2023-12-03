from unittest.mock import ANY

from solutions import BaseTestCase
from solutions.year_2015.day_13.solution import Year2015Day13


class TestSolution(BaseTestCase):
    def setUp(self):
        self.solution = Year2015Day13()
        self.answers = (709, 668)


class TestSample(BaseTestCase):
    def setUp(self):
        self.solution = Year2015Day13("sample.txt")
        self.answers = (330, ANY)
