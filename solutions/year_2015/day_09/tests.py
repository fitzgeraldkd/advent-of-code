from solutions import BaseTestCase
from solutions.year_2015.day_09.solution import Year2015Day09


class TestSolution(BaseTestCase):
    def setUp(self):
        self.solution = Year2015Day09()
        self.answers = (251, 898)


class TestSample(BaseTestCase):
    def setUp(self):
        self.solution = Year2015Day09("sample.txt")
        self.answers = (605, 982)
