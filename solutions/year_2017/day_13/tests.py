from solutions import BaseTestCase
from solutions.year_2017.day_13.solution import Year2017Day13


class TestSolution(BaseTestCase):
    def setUp(self):
        self.solution = Year2017Day13()
        self.answers = (1476, 3937334)


class TestSample(BaseTestCase):
    def setUp(self):
        self.solution = Year2017Day13("sample.txt")
        self.answers = (24, 10)
