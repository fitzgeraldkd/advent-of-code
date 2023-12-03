from solutions import BaseTestCase
from solutions.year_2015.day_14.solution import Year2015Day14


class TestSolution(BaseTestCase):
    def setUp(self):
        self.solution = Year2015Day14()
        self.answers = (2640, 1102)


class TestSample(BaseTestCase):
    def setUp(self):
        self.solution = Year2015Day14("sample.txt")
        self.solution.RACE_DURATION = 1000
        self.answers = (1120, 689)
