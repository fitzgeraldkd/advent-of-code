from solutions import BaseTestCase
from solutions.year_2017.day_05.solution import Year2017Day05


class TestSolution(BaseTestCase):
    def setUp(self):
        self.solution = Year2017Day05()
        self.answers = (374269, 27720699)


class TestSample(BaseTestCase):
    def setUp(self):
        self.solution = Year2017Day05("sample.txt")
        self.answers = (5, 10)
