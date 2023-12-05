from solutions import BaseTestCase
from solutions.year_2020.day_18.solution import Year2020Day18


class TestSolution(BaseTestCase):
    def setUp(self):
        self.solution = Year2020Day18()
        self.answers = (654686398176, 8952864356993)


class TestSample(BaseTestCase):
    def setUp(self):
        self.solution = Year2020Day18("sample.txt")
        self.answers = (26457, 694173)
