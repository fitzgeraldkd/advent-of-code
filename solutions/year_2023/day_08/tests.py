from unittest.mock import ANY

from solutions import BaseTestCase
from solutions.year_2023.day_08.solution import Year2023Day08


class TestSolution(BaseTestCase):
    def setUp(self):
        self.solution = Year2023Day08()
        self.answers = (14257, 16187743689077)


class TestSample1(BaseTestCase):
    def setUp(self):
        self.solution = Year2023Day08("sample1.txt")
        self.answers = (2, ANY)


class TestSample2(BaseTestCase):
    def setUp(self):
        self.solution = Year2023Day08("sample2.txt")
        self.answers = (6, ANY)


class TestSample3(BaseTestCase):
    def setUp(self):
        self.solution = Year2023Day08("sample3.txt")
        self.answers = (ANY, 6)

    def test_part_1(self):
        """
        This sample crashes part 1.
        """
        pass
