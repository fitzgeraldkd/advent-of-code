from solutions import BaseTestCase
from solutions.year_2015.day_08.solution import Year2015Day08


class TestSolution(BaseTestCase):
    def setUp(self):
        self.solution = Year2015Day08()
        self.answers = (1333, 2046)


class TestSample(BaseTestCase):
    def setUp(self):
        self.solution = Year2015Day08("sample.txt")
        self.answers = (12, 19)
