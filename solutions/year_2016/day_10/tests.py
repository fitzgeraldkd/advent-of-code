from unittest.mock import ANY, patch

from solutions import BaseTestCase
from solutions.year_2016.day_10.solution import Year2016Day10


class TestSolution(BaseTestCase):
    def setUp(self):
        self.solution = Year2016Day10()
        self.answers = (56, 7847)


class TestSample(BaseTestCase):
    def setUp(self):
        self.solution = Year2016Day10("sample.txt")
        self.answers = (2, ANY)

    @patch.object(Year2016Day10, "TARGETS", [2, 5])
    def test_part_1(self):
        return super().test_part_1()
