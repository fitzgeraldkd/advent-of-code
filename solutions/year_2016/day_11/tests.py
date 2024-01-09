from unittest.mock import ANY, patch

from solutions import BaseTestCase
from solutions.year_2016.day_11.solution import Year2016Day11


class TestSolution(BaseTestCase):
    def setUp(self):
        self.solution = Year2016Day11()
        self.answers = (33, 57)


class TestSample(BaseTestCase):
    hardcoded_inputs = {
        "E": 1,
        "HM": 1,
        "LM": 1,
        "HG": 2,
        "LG": 3,
    }

    def setUp(self):
        self.solution = Year2016Day11("sample.txt")
        self.answers = (11, ANY)

    @patch.object(Year2016Day11, "inputs", hardcoded_inputs)
    def test_part_1(self):
        return super().test_part_1()

    @patch.object(Year2016Day11, "inputs", hardcoded_inputs)
    def test_part_2(self):
        return super().test_part_2()
