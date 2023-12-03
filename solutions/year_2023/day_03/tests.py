from solutions import BaseTestCase
from solutions.year_2023.day_03.solution import Year2023Day03


class TestSolution(BaseTestCase):
    def setUp(self):
        self.solution = Year2023Day03()
        self.answers = (530849, 84900879)


class TestSample(BaseTestCase):
    def setUp(self):
        self.solution = Year2023Day03("sample.txt")
        self.answers = (4361, 467835)
