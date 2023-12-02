from solutions import BaseTestCase
from solutions.year_2018.day_04.solution import Year2018Day04


class TestSolution(BaseTestCase):
    def setUp(self):
        self.solution = Year2018Day04()
        self.answers = (19025, 23776)


class TestSample(BaseTestCase):
    def setUp(self):
        self.solution = Year2018Day04("sample.txt")
        self.answers = (240, 4455)
