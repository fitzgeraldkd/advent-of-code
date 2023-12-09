from solutions import BaseTestCase
from solutions.year_2023.day_09.solution import Year2023Day09


class TestSolution(BaseTestCase):
    def setUp(self):
        self.solution = Year2023Day09()
        self.answers = (1939607039, 1041)


class TestSample(BaseTestCase):
    def setUp(self):
        self.solution = Year2023Day09("sample.txt")
        self.answers = (114, 2)
