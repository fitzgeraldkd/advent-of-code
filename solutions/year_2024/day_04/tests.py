from solutions import BaseTestCase
from solutions.year_2024.day_04.solution import Year2024Day04


class TestSolution(BaseTestCase):
    def setUp(self):
        self.solution = Year2024Day04()
        self.answers = (2496, 1967)


class TestSample(BaseTestCase):
    def setUp(self):
        self.solution = Year2024Day04("sample.txt")
        self.answers = (18, 9)
