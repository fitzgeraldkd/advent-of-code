from unittest.mock import ANY, patch

from solutions import BaseTestCase
from solutions.year_2016.day_13.solution import Year2016Day13


class TestSolution(BaseTestCase):
    def setUp(self):
        self.solution = Year2016Day13()
        self.answers = (86, 127)


class TestSample(BaseTestCase):
    def setUp(self):
        self.solution = Year2016Day13("sample.txt")
        self.answers = (11, ANY)

    @patch.object(Year2016Day13, "TARGET", (7, 4))
    def test_part_1(self):
        return super().test_part_1()
