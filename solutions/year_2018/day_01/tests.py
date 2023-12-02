from unittest.mock import patch

from solutions import BaseTestCase
from solutions.year_2018.day_01.solution import Year2018Day01


class TestSolution(BaseTestCase):
    def setUp(self):
        self.solution = Year2018Day01()
        self.answers = (442, 59908)


class TestSamples(BaseTestCase):
    def setUp(self):
        self.solution = Year2018Day01()

    def test_part_1(self):
        with patch.object(Year2018Day01, "inputs", [1, -2, 3, 1]):
            self.assertEqual(self.solution.part_1(), 3)

        with patch.object(Year2018Day01, "inputs", [1, 1, 1]):
            self.assertEqual(self.solution.part_1(), 3)

        with patch.object(Year2018Day01, "inputs", [1, 1, -2]):
            self.assertEqual(self.solution.part_1(), 0)

        with patch.object(Year2018Day01, "inputs", [-1, -2, -3]):
            self.assertEqual(self.solution.part_1(), -6)

    def test_part_2(self):
        with patch.object(Year2018Day01, "inputs", [1, -2, 3, 1]):
            self.assertEqual(self.solution.part_2(), 2)

        with patch.object(Year2018Day01, "inputs", [1, -1]):
            self.assertEqual(self.solution.part_2(), 0)

        with patch.object(Year2018Day01, "inputs", [3, 3, 4, -2, -4]):
            self.assertEqual(self.solution.part_2(), 10)

        with patch.object(Year2018Day01, "inputs", [-6, 3, 8, 5, -6]):
            self.assertEqual(self.solution.part_2(), 5)

        with patch.object(Year2018Day01, "inputs", [7, 7, -2, -7, -4]):
            self.assertEqual(self.solution.part_2(), 14)
