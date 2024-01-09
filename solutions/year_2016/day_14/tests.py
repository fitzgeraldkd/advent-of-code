from solutions import BaseTestCase
from solutions.year_2016.day_14.solution import Year2016Day14


class TestSolution(BaseTestCase):
    def setUp(self):
        self.solution = Year2016Day14()
        self.answers = (25427, 22045)


class TestSample(BaseTestCase):
    def setUp(self):
        self.solution = Year2016Day14("sample.txt")
        self.answers = (22728, 22551)
