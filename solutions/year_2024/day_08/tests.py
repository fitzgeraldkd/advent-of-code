from solutions import BaseTestCase
from solutions.year_2024.day_08.solution import Year2024Day08


class TestSolution(BaseTestCase):
    def setUp(self):
        self.solution = Year2024Day08()
        self.answers = (261, 898)


class TestSample(BaseTestCase):
    def setUp(self):
        self.solution = Year2024Day08("sample.txt")
        self.answers = (14, 34)
