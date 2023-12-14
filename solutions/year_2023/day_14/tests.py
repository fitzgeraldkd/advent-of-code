from solutions import BaseTestCase
from solutions.year_2023.day_14.solution import Year2023Day14


class TestSolution(BaseTestCase):
    def setUp(self):
        self.solution = Year2023Day14()
        self.answers = (107951, 95736)


class TestSample(BaseTestCase):
    def setUp(self):
        self.solution = Year2023Day14("sample.txt")
        self.answers = (136, 64)
