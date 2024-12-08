from solutions import BaseTestCase
from solutions.year_2024.day_07.solution import Year2024Day07


class TestSolution(BaseTestCase):
    def setUp(self):
        self.solution = Year2024Day07()
        self.answers = (7885693428401, 348360680516005)


class TestSample(BaseTestCase):
    def setUp(self):
        self.solution = Year2024Day07("sample.txt")
        self.answers = (3749, 11387)
