# from unittest.mock import pat
from solutions import BaseTestCase
from solutions.year_2024.day_18.solution import Year2024Day18


class TestSolution(BaseTestCase):
    def setUp(self):
        self.solution = Year2024Day18()
        self.answers = (436, "61,50")


class TestSample(BaseTestCase):
    def setUp(self):
        self.solution = Year2024Day18("sample.txt")
        self.solution.PART_1_BYTES = 12
        self.solution.END = (6, 6)
        self.answers = (22, "6,1")
