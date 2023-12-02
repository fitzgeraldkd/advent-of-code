from solutions import BaseTestCase
from solutions.year_2018.day_05.solution import Year2018Day05


class TestSolution(BaseTestCase):
    def setUp(self):
        self.solution = Year2018Day05()
        self.answers = (11540, 6918)


class TestSample(BaseTestCase):
    def setUp(self):
        self.solution = Year2018Day05("sample.txt")
        self.answers = (10, 4)
