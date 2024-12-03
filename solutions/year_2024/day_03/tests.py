from solutions import BaseTestCase
from solutions.year_2024.day_03.solution import Year2024Day03


class TestSolution(BaseTestCase):
    def setUp(self):
        self.solution = Year2024Day03()
        self.answers = (161289189, 83595109)


class TestSample(BaseTestCase):
    def setUp(self):
        self.solution = Year2024Day03("sample.txt")
        self.answers = (161, 48)
