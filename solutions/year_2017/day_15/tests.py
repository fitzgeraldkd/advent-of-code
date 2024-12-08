from solutions import BaseTestCase
from solutions.year_2017.day_15.solution import Year2017Day15


class TestSolution(BaseTestCase):
    def setUp(self):
        self.solution = Year2017Day15()
        self.answers = (600, 313)


class TestSample(BaseTestCase):
    def setUp(self):
        self.solution = Year2017Day15("sample.txt")
        self.answers = (588, 309)
