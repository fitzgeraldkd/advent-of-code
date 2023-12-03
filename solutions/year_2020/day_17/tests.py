from solutions import BaseTestCase
from solutions.year_2020.day_17.solution import Year2020Day17


class TestSolution(BaseTestCase):
    def setUp(self):
        self.solution = Year2020Day17()
        self.answers = (267, 1812)


class TestSample(BaseTestCase):
    def setUp(self):
        self.solution = Year2020Day17("sample.txt")
        self.answers = (112, 848)
