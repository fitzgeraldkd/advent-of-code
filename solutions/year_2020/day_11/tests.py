from solutions import BaseTestCase
from solutions.year_2020.day_11.solution import Year2020Day11


class TestSolution(BaseTestCase):
    def setUp(self):
        self.solution = Year2020Day11(__file__)
        self.answers = (2166, 1955)


class TestSample(BaseTestCase):
    def setUp(self):
        self.solution = Year2020Day11(__file__, "sample.txt")
        self.answers = (37, 26)
