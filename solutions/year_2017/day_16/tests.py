from solutions import BaseTestCase
from solutions.year_2017.day_16.solution import Year2017Day16


class TestSolution(BaseTestCase):
    def setUp(self):
        self.solution = Year2017Day16()
        self.answers = ("fnloekigdmpajchb", "amkjepdhifolgncb")


class TestSample(BaseTestCase):
    def setUp(self):
        self.solution = Year2017Day16("sample.txt")
        self.solution.STARTING_LINE = "abcde"
        self.answers = ("baedc", None)

    def test_part_2(self):
        pass
