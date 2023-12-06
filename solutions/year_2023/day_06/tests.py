from solutions import BaseTestCase
from solutions.year_2023.day_06.solution import Year2023Day06


class TestSolution(BaseTestCase):
    def setUp(self):
        self.solution = Year2023Day06()
        self.answers = (3316275, 27102791)


class TestSample(BaseTestCase):
    def setUp(self):
        self.solution = Year2023Day06("sample.txt")
        self.answers = (288, 71503)
