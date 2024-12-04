from solutions import BaseTestCase
from solutions.year_2017.day_06.solution import Year2017Day06


class TestSolution(BaseTestCase):
    def setUp(self):
        self.solution = Year2017Day06()
        self.answers = (11137, 1037)


class TestSample(BaseTestCase):
    def setUp(self):
        self.solution = Year2017Day06("sample.txt")
        self.answers = (5, 4)
