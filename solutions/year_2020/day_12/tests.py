from solutions import BaseTestCase
from solutions.year_2020.day_12.solution import Year2020Day12


class TestSolution(BaseTestCase):
    def setUp(self):
        self.solution = Year2020Day12()
        self.answers = (1186, 47806)


class TestSample(BaseTestCase):
    def setUp(self):
        self.solution = Year2020Day12("sample.txt")
        self.answers = (25, 286)
