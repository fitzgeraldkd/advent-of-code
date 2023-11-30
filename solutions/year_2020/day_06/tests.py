from solutions import BaseTestCase
from solutions.year_2020.day_06.solution import Year2020Day06


class TestSolution(BaseTestCase):
    def setUp(self):
        self.solution = Year2020Day06(__file__)
        self.answers = (6778, 3406)


class TestSample(BaseTestCase):
    def setUp(self):
        self.solution = Year2020Day06(__file__, "sample.txt")
        self.answers = (11, 6)
