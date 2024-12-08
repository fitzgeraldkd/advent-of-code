from unittest.mock import patch

from solutions import BaseTestCase
from solutions.year_2017.day_11.solution import Year2017Day11


class TestSolution(BaseTestCase):
    def setUp(self):
        self.solution = Year2017Day11()
        self.answers = (696, 1461)


class TestSample(BaseTestCase):
    def setUp(self):
        self.solution = Year2017Day11("sample.txt")

    def test_part_1(self):
        with patch.object(Year2017Day11, "inputs", ["ne", "ne", "ne"]):
            self.assertEqual(self.solution.part_1(), 3)
        with patch.object(Year2017Day11, "inputs", ["ne", "ne", "sw", "sw"]):
            self.assertEqual(self.solution.part_1(), 0)
        with patch.object(Year2017Day11, "inputs", ["ne", "ne", "s", "s"]):
            self.assertEqual(self.solution.part_1(), 2)
        with patch.object(Year2017Day11, "inputs", ["se", "sw", "se", "sw", "sw"]):
            self.assertEqual(self.solution.part_1(), 3)
        with patch.object(Year2017Day11, "inputs", ["ne", "se"]):
            self.assertEqual(self.solution.part_1(), 2)

    def test_part_2(self):
        pass
