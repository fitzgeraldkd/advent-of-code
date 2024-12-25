from solutions import BaseTestCase
from solutions.year_2024.day_25.solution import Year2024Day25


class TestSolution(BaseTestCase):
    def setUp(self):
        self.solution = Year2024Day25()
        self.answers = (3249, None)


class TestSample(BaseTestCase):
    def setUp(self):
        self.solution = Year2024Day25("sample.txt")
        self.answers = (3, None)
