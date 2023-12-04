from solutions import BaseTestCase
from solutions.year_2023.day_04.solution import Year2023Day04


class TestSolution(BaseTestCase):
    def setUp(self):
        self.solution = Year2023Day04()
        self.answers = (15268, 6283755)


class TestSample(BaseTestCase):
    def setUp(self):
        self.solution = Year2023Day04("sample.txt")
        self.answers = (13, 30)
