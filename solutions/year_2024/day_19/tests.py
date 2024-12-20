from solutions import BaseTestCase
from solutions.year_2024.day_19.solution import Year2024Day19


class TestSolution(BaseTestCase):
    def setUp(self):
        self.solution = Year2024Day19()
        self.answers = (374, 1100663950563322)


class TestSample(BaseTestCase):
    def setUp(self):
        self.solution = Year2024Day19("sample.txt")
        self.answers = (6, 16)
