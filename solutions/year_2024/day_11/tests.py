from solutions import BaseTestCase
from solutions.year_2024.day_11.solution import Year2024Day11


class TestSolution(BaseTestCase):
    def setUp(self):
        self.solution = Year2024Day11()
        self.answers = (197357, 234568186890978)


class TestSample(BaseTestCase):
    def setUp(self):
        self.solution = Year2024Day11("sample.txt")
        self.answers = (55312, 65601038650482)
