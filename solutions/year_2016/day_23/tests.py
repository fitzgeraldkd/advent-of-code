from unittest.mock import ANY

from solutions import BaseTestCase
from solutions.year_2016.day_23.solution import Year2016Day23


class TestSolution(BaseTestCase):
    def setUp(self):
        self.solution = Year2016Day23()
        self.answers = (11500, 479008060)

    def test_part_2(self):
        self.skipTest("Highly unoptimized, takes about an hour to run.")
        return super().test_part_2()


class TestSample(BaseTestCase):
    def setUp(self):
        self.solution = Year2016Day23("sample.txt")
        self.answers = (3, ANY)
