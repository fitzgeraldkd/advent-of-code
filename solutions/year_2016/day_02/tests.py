from solutions import BaseTestCase
from solutions.year_2016.day_02.solution import Year2016Day02


class TestSolution(BaseTestCase):
    def setUp(self):
        self.solution = Year2016Day02()
        self.answers = ("47978", "659AD")


class TestSample(BaseTestCase):
    def setUp(self):
        self.solution = Year2016Day02("sample.txt")
        self.answers = ("1985", "5DB3")
