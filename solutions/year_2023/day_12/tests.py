from solutions import BaseTestCase
from solutions.year_2023.day_12.solution import Year2023Day12


class TestSolution(BaseTestCase):
    def setUp(self):
        self.solution = Year2023Day12()
        self.answers = (None, None)


class TestSample(BaseTestCase):
    def setUp(self):
        self.solution = Year2023Day12("sample.txt")
        self.answers = (None, None)
