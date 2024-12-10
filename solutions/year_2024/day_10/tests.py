from solutions import BaseTestCase
from solutions.year_2024.day_10.solution import Year2024Day10


class TestSolution(BaseTestCase):
    def setUp(self):
        self.solution = Year2024Day10()
        self.answers = (822, 1801)


class TestSample(BaseTestCase):
    def setUp(self):
        self.solution = Year2024Day10("sample.txt")
        self.answers = (36, 81)
