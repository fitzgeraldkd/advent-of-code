from solutions import BaseTestCase
from solutions.year_2024.day_13.solution import Year2024Day13


class TestSolution(BaseTestCase):
    def setUp(self):
        self.solution = Year2024Day13()
        self.answers = (39748, 74478585072604)


class TestSample(BaseTestCase):
    def setUp(self):
        self.solution = Year2024Day13("sample.txt")
        self.answers = (480, 875318608908)
