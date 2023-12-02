from solutions import BaseTestCase
from solutions.year_2020.day_10.solution import Year2020Day10


class TestSolution(BaseTestCase):
    def setUp(self):
        self.solution = Year2020Day10()
        self.answers = (2475, 442136281481216)


class TestSample1(BaseTestCase):
    def setUp(self):
        self.solution = Year2020Day10("sample1.txt")
        self.answers = (35, 8)


class TestSample2(BaseTestCase):
    def setUp(self):
        self.solution = Year2020Day10("sample2.txt")
        self.answers = (220, 19208)
