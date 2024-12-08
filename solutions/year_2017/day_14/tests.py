from solutions import BaseTestCase
from solutions.year_2017.day_14.solution import Year2017Day14


class TestSolution(BaseTestCase):
    def setUp(self):
        self.solution = Year2017Day14()
        self.answers = (8230, 1103)


class TestSample(BaseTestCase):
    def setUp(self):
        self.solution = Year2017Day14("sample.txt")
        self.answers = (8108, 1242)
