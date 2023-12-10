from unittest.mock import ANY

from solutions import BaseTestCase
from solutions.year_2023.day_10.solution import Year2023Day10


class TestSolution(BaseTestCase):
    def setUp(self):
        self.solution = Year2023Day10()
        self.answers = (7086, 317)


class TestSample1(BaseTestCase):
    def setUp(self):
        self.solution = Year2023Day10("sample1.txt")
        self.answers = (4, ANY)


class TestSample2(BaseTestCase):
    def setUp(self):
        self.solution = Year2023Day10("sample2.txt")
        self.answers = (8, ANY)


class TestSample3(BaseTestCase):
    def setUp(self):
        self.solution = Year2023Day10("sample3.txt")
        self.answers = (ANY, 4)


class TestSample4(BaseTestCase):
    def setUp(self):
        self.solution = Year2023Day10("sample4.txt")
        self.answers = (ANY, 8)


class TestSample5(BaseTestCase):
    def setUp(self):
        self.solution = Year2023Day10("sample5.txt")
        self.answers = (ANY, 10)
