from solutions import BaseTestCase
from solutions.year_2024.day_01.solution import Year2024Day01


class TestSolution(BaseTestCase):
    def setUp(self):
        self.solution = Year2024Day01()
        self.answers = (1189304, 24349736)


class TestSample(BaseTestCase):
    def setUp(self):
        self.solution = Year2024Day01("sample.txt")
        self.answers = (11, 31)
