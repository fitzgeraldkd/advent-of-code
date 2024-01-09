from solutions import BaseTestCase
from solutions.year_2016.day_06.solution import Year2016Day06


class TestSolution(BaseTestCase):
    def setUp(self):
        self.solution = Year2016Day06()
        self.answers = ("qtbjqiuq", "akothqli")


class TestSample(BaseTestCase):
    def setUp(self):
        self.solution = Year2016Day06("sample.txt")
        self.answers = ("easter", "advent")
