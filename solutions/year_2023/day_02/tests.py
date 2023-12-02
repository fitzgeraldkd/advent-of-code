from solutions import BaseTestCase
from solutions.year_2023.day_02.solution import Year2023Day02


class TestSolution(BaseTestCase):
    def setUp(self):
        self.solution = Year2023Day02()
        self.answers = (2416, 63307)


class TestSample(BaseTestCase):
    def setUp(self):
        self.solution = Year2023Day02("sample.txt")
        self.answers = (8, 2286)
