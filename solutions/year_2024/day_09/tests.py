from solutions import BaseTestCase
from solutions.year_2024.day_09.solution import Year2024Day09


class TestSolution(BaseTestCase):
    def setUp(self):
        self.solution = Year2024Day09()
        self.answers = (6299243228569, 6326952672104)


class TestSample(BaseTestCase):
    def setUp(self):
        self.solution = Year2024Day09("sample.txt")
        self.answers = (1928, 2858)
