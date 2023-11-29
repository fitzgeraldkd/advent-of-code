from unittest.mock import patch

from solutions import BaseTestCase
from solutions.year_2015.day_03.solution import Year2015Day03


class TestSolution(BaseTestCase):
    def setUp(self):
        self.solution = Year2015Day03(__file__)
        self.answers = (2081, 2341)


class TestSample(BaseTestCase):
    def setUp(self):
        self.solution = Year2015Day03(__file__)

    def test_part_1(self):
        with patch.object(Year2015Day03, "inputs", ">"):
            self.assertEqual(self.solution.part_1(), 2)

        with patch.object(Year2015Day03, "inputs", "^>v<"):
            self.assertEqual(self.solution.part_1(), 4)

        with patch.object(Year2015Day03, "inputs", "^v^v^v^v^v"):
            self.assertEqual(self.solution.part_1(), 2)

    def test_part_2(self):
        with patch.object(Year2015Day03, "inputs", "^v"):
            self.assertEqual(self.solution.part_2(), 3)

        with patch.object(Year2015Day03, "inputs", "^>v<"):
            self.assertEqual(self.solution.part_2(), 3)

        with patch.object(Year2015Day03, "inputs", "^v^v^v^v^v"):
            self.assertEqual(self.solution.part_2(), 11)
