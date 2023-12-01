from solutions import BaseTestCase
from solutions.year_2020.day_08.solution import Year2020Day08


class TestSolution(BaseTestCase):
    def setUp(self):
        self.solution = Year2020Day08(__file__)
        self.answers = (1586, 703)


class TestSample(BaseTestCase):
    def setUp(self):
        self.solution = Year2020Day08(__file__, "sample.txt")
        self.answers = (5, 8)
