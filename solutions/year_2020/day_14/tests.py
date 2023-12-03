from unittest.mock import ANY

from solutions import BaseTestCase
from solutions.year_2020.day_14.solution import Year2020Day14


class TestSolution(BaseTestCase):
    def setUp(self):
        self.solution = Year2020Day14()
        self.answers = (17765746710228, 4401465949086)


class TestSample1(BaseTestCase):
    def setUp(self):
        self.solution = Year2020Day14("sample1.txt")
        self.answers = (165, None)

    def test_part_2(self):
        """
        Times out from the number of floating bits.
        """
        pass


class TestSample2(BaseTestCase):
    def setUp(self):
        self.solution = Year2020Day14("sample2.txt")
        self.answers = (ANY, 208)
