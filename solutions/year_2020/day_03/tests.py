from solutions import BaseTestCase
from solutions.year_2020.day_03.solution import Year2020Day03


class TestSolution(BaseTestCase):
    def setUp(self):
        self.solution = Year2020Day03(__file__)
        self.answers = (270, 2122848000)


class TestSample(BaseTestCase):
    def setUp(self):
        self.solution = Year2020Day03(__file__, "sample.txt")
        self.answers = (7, 336)
