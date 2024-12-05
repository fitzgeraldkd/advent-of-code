from solutions import BaseTestCase
from solutions.year_2017.day_07.solution import Year2017Day07


class TestSolution(BaseTestCase):
    def setUp(self):
        self.solution = Year2017Day07()
        self.answers = ("bsfpjtc", 529)


class TestSample(BaseTestCase):
    def setUp(self):
        self.solution = Year2017Day07("sample.txt")
        self.answers = ("tknk", 60)
