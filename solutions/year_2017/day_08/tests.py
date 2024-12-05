from solutions import BaseTestCase
from solutions.year_2017.day_08.solution import Year2017Day08


class TestSolution(BaseTestCase):
    def setUp(self):
        self.solution = Year2017Day08()
        self.answers = (5946, 6026)


class TestSample(BaseTestCase):
    def setUp(self):
        self.solution = Year2017Day08("sample.txt")
        self.answers = (1, 10)
