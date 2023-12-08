from solutions import BaseTestCase
from solutions.year_2023.day_07.solution import Year2023Day07


class TestSolution(BaseTestCase):
    def setUp(self):
        self.solution = Year2023Day07()
        self.answers = (246163188, 245794069)


class TestSample(BaseTestCase):
    def setUp(self):
        self.solution = Year2023Day07("sample.txt")
        self.answers = (6440, 5905)
