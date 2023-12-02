from solutions import BaseTestCase
from solutions.year_2020.day_02.solution import Year2020Day02


class TestSolution(BaseTestCase):
    def setUp(self):
        self.solution = Year2020Day02()
        self.answers = (434, 509)


class TestSample(BaseTestCase):
    def setUp(self):
        self.solution = Year2020Day02("sample.txt")
        self.answers = (2, 1)
