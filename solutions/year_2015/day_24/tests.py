from solutions import BaseTestCase
from solutions.year_2015.day_24.solution import Year2015Day24


class TestSolution(BaseTestCase):
    def setUp(self):
        self.solution = Year2015Day24()
        self.answers = (10439961859, 72050269)


class TestSample(BaseTestCase):
    def setUp(self):
        self.solution = Year2015Day24("sample.txt")
        self.answers = (99, 44)
