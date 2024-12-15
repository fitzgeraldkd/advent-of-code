from solutions import BaseTestCase
from solutions.year_2024.day_15.solution import Year2024Day15


class TestSolution(BaseTestCase):
    def setUp(self):
        self.solution = Year2024Day15()
        self.answers = (1538871, 1543338)


class TestSample(BaseTestCase):
    def setUp(self):
        self.solution = Year2024Day15("sample.txt")
        self.answers = (10092, 9021)
