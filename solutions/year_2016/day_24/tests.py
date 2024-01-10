from unittest.mock import ANY

from solutions import BaseTestCase
from solutions.year_2016.day_24.solution import Year2016Day24


class TestSolution(BaseTestCase):
    def setUp(self):
        self.solution = Year2016Day24()
        self.answers = (502, 724)


class TestSample(BaseTestCase):
    def setUp(self):
        self.solution = Year2016Day24("sample.txt")
        self.answers = (14, ANY)
