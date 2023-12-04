from solutions import BaseTestCase
from solutions.year_2015.day_17.solution import Year2015Day17


class TestSolution(BaseTestCase):
    def setUp(self):
        self.solution = Year2015Day17()
        self.answers = (4372, 4)


class TestSample(BaseTestCase):
    def setUp(self):
        self.solution = Year2015Day17("sample.txt")
        self.solution.TARGET_VOLUME = 25
        self.answers = (4, 3)
