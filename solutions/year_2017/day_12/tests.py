from solutions import BaseTestCase
from solutions.year_2017.day_12.solution import Year2017Day12


class TestSolution(BaseTestCase):
    def setUp(self):
        self.solution = Year2017Day12()
        self.answers = (378, 204)


class TestSample(BaseTestCase):
    def setUp(self):
        self.solution = Year2017Day12("sample.txt")
        self.answers = (6, 2)
