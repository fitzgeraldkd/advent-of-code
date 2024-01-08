from solutions import BaseTestCase
from solutions.year_2015.day_25.solution import Year2015Day25


class TestSolution(BaseTestCase):
    def setUp(self):
        self.solution = Year2015Day25()
        self.answers = (2650453, None)


class TestSample(BaseTestCase):
    def setUp(self):
        self.solution = Year2015Day25("sample.txt")
        self.answers = (31916031, None)
