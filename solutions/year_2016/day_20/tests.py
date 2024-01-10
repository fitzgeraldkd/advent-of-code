from unittest.mock import patch

from solutions import BaseTestCase
from solutions.year_2016.day_20.solution import Year2016Day20


class TestSolution(BaseTestCase):
    def setUp(self):
        self.solution = Year2016Day20()
        self.answers = (17348574, 104)


class TestSample(BaseTestCase):
    def setUp(self):
        self.solution = Year2016Day20("sample.txt")
        self.answers = (3, 2)

    @patch.object(Year2016Day20, "MAX_ADDRESS", 9)
    def test_part_2(self):
        return super().test_part_2()
