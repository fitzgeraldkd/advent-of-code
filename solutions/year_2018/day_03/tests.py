from solutions import BaseTestCase
from solutions.year_2018.day_03.solution import Year2018Day03


class TestSolution(BaseTestCase):
    def setUp(self):
        self.solution = Year2018Day03(__file__)
        self.answers = (98005, 331)


class TestSample(BaseTestCase):
    def setUp(self):
        self.solution = Year2018Day03(__file__, "sample.txt")
        self.answers = (4, 3)
