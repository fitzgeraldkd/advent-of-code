from solutions import BaseTestCase
from solutions.year_2023.day_16.solution import Year2023Day16


class TestSolution(BaseTestCase):
    def setUp(self):
        self.solution = Year2023Day16()
        self.answers = (7477, 7853)


class TestSample(BaseTestCase):
    def setUp(self):
        self.solution = Year2023Day16("sample.txt")
        self.answers = (46, 51)
