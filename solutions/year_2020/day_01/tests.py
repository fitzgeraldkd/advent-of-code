from solutions import BaseTestCase
from solutions.year_2020.day_01.solution import Year2020Day01


class TestSolution(BaseTestCase):
    def setUp(self):
        self.solution = Year2020Day01(__file__)
        self.answers = (355875, 140379120)


class TestSample(BaseTestCase):
    def setUp(self):
        self.solution = Year2020Day01(__file__, "sample.txt")
        self.answers = (514579, 241861950)
