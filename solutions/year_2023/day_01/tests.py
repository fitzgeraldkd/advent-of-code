from unittest.mock import ANY

from solutions import BaseTestCase
from solutions.year_2023.day_01.solution import Year2023Day01


class TestSolution(BaseTestCase):
    def setUp(self):
        self.solution = Year2023Day01(__file__)
        self.answers = (56042, 55358)


class TestSample1(BaseTestCase):
    def setUp(self):
        self.solution = Year2023Day01(__file__, "sample1.txt")
        self.answers = (142, ANY)


class TestSample2(BaseTestCase):
    def setUp(self):
        self.solution = Year2023Day01(__file__, "sample2.txt")
        self.answers = (ANY, 281)

    def test_part_1(self):
        """
        The solution for part 1 crashes with this input.
        """
        pass
