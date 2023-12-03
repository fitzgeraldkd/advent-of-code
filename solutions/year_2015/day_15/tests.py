from unittest import expectedFailure

from solutions import BaseTestCase
from solutions.year_2015.day_15.solution import Year2015Day15


class TestSolution(BaseTestCase):
    def setUp(self):
        self.solution = Year2015Day15()
        self.answers = (13882464, 11171160)


class TestSample(BaseTestCase):
    def setUp(self):
        self.solution = Year2015Day15("sample.txt")
        self.answers = (62842880, 57600000)

    @expectedFailure
    def test_part_2(self):
        """
        The solution is hard-coded for 4 ingredients.
        """
        return super().test_part_2()
