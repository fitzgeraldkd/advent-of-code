from unittest.mock import ANY, patch

from solutions import BaseTestCase
from solutions.year_2016.day_18.solution import Year2016Day18


class TestSolution(BaseTestCase):
    def setUp(self):
        self.solution = Year2016Day18()
        self.answers = (1987, 19984714)


class TestSample(BaseTestCase):
    def setUp(self):
        self.solution = Year2016Day18("sample.txt")
        self.answers = (38, ANY)

    @patch.object(Year2016Day18, "PART_1_ROWS", 10)
    def test_part_1(self):
        return super().test_part_1()
