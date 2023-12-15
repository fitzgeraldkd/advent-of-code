from solutions import BaseTestCase
from solutions.year_2023.day_15.solution import Year2023Day15


class TestSolution(BaseTestCase):
    def setUp(self):
        self.solution = Year2023Day15()
        self.answers = (518107, 303404)


class TestSample(BaseTestCase):
    def setUp(self):
        self.solution = Year2023Day15("sample.txt")
        self.answers = (1320, 145)
