from solutions import BaseTestCase
from solutions.year_2024.day_02.solution import Year2024Day02


class TestSolution(BaseTestCase):
    def setUp(self):
        self.solution = Year2024Day02()
        self.answers = (524, 569)


class TestSample(BaseTestCase):
    def setUp(self):
        self.solution = Year2024Day02("sample.txt")
        self.answers = (2, 4)
