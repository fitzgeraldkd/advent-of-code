from solutions import BaseTestCase
from solutions.year_2024.day_12.solution import Year2024Day12


class TestSolution(BaseTestCase):
    def setUp(self):
        self.solution = Year2024Day12()
        self.answers = (1473620, 902620)


class TestSample(BaseTestCase):
    def setUp(self):
        self.solution = Year2024Day12("sample.txt")
        self.answers = (1930, 1206)
