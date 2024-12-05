from solutions import BaseTestCase
from solutions.year_2024.day_05.solution import Year2024Day05


class TestSolution(BaseTestCase):
    def setUp(self):
        self.solution = Year2024Day05()
        self.answers = (5991, 5479)


class TestSample(BaseTestCase):
    def setUp(self):
        self.solution = Year2024Day05("sample.txt")
        self.answers = (143, 123)
