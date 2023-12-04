from solutions import BaseTestCase
from solutions.year_2015.day_19.solution import Year2015Day19


class TestSolution(BaseTestCase):
    def setUp(self):
        self.solution = Year2015Day19()
        self.answers = (576, 207)


class TestSample1(BaseTestCase):
    def setUp(self):
        self.solution = Year2015Day19("sample1.txt")
        self.answers = (4, 3)


class TestSample2(BaseTestCase):
    def setUp(self):
        self.solution = Year2015Day19("sample2.txt")
        self.answers = (7, 6)
