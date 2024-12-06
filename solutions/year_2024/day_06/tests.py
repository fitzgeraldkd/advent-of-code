from solutions import BaseTestCase
from solutions.year_2024.day_06.solution import Year2024Day06


class TestSolution(BaseTestCase):
    def setUp(self):
        self.solution = Year2024Day06()
        self.answers = (4559, 1604)


class TestSample(BaseTestCase):
    def setUp(self):
        self.solution = Year2024Day06("sample.txt")
        self.answers = (41, 6)
