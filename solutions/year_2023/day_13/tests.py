from solutions import BaseTestCase
from solutions.year_2023.day_13.solution import Year2023Day13


class TestSolution(BaseTestCase):
    def setUp(self):
        self.solution = Year2023Day13()
        self.answers = (31877, 42996)


class TestSample(BaseTestCase):
    def setUp(self):
        self.solution = Year2023Day13("sample.txt")
        self.answers = (405, 400)
