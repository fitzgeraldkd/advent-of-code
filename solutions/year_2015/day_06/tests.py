from unittest.mock import ANY

from solutions import BaseTestCase
from solutions.year_2015.day_06.solution import Year2015Day06


class TestSolution(BaseTestCase):
    def setUp(self):
        self.solution = Year2015Day06(__file__)
        self.answers = (569999, 17836115)


class TestSample1(BaseTestCase):
    def setUp(self):
        self.solution = Year2015Day06(__file__, "sample1.txt")
        self.answers = (998996, ANY)


class TestSample2(BaseTestCase):
    def setUp(self):
        self.solution = Year2015Day06(__file__, "sample2.txt")
        self.answers = (ANY, 2000001)
