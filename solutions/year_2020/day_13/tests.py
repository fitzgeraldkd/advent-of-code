from solutions import BaseTestCase
from solutions.year_2020.day_13.solution import Year2020Day13


class TestSolution(BaseTestCase):
    def setUp(self):
        self.solution = Year2020Day13(__file__)
        self.answers = (2045, 402251700208309)


class TestSample(BaseTestCase):
    def setUp(self):
        self.solution = Year2020Day13(__file__, "sample.txt")
        self.answers = (295, 1068781)
