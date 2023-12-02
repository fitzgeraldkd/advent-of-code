from solutions import BaseTestCase
from solutions.year_2020.day_09.solution import Year2020Day09


class TestSolution(BaseTestCase):
    def setUp(self):
        self.solution = Year2020Day09()
        self.answers = (258585477, 36981213)


class TestSample(BaseTestCase):
    def setUp(self):
        self.solution = Year2020Day09("sample.txt")
        self.solution.PREAMBLE = 5
        self.answers = (127, 62)
