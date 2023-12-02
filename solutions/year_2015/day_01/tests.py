from unittest.mock import patch

from solutions import BaseTestCase
from solutions.year_2015.day_01.solution import Year2015Day01


class TestSolution(BaseTestCase):
    def setUp(self):
        self.solution = Year2015Day01()
        self.answers = (138, 1771)


class TestSample(BaseTestCase):
    def setUp(self):
        self.solution = Year2015Day01()

    def test_part_1(self):
        with patch.object(Year2015Day01, "inputs", "(())"):
            self.assertEqual(self.solution.part_1(), 0)

        with patch.object(Year2015Day01, "inputs", "()()"):
            self.assertEqual(self.solution.part_1(), 0)

        with patch.object(Year2015Day01, "inputs", "((("):
            self.assertEqual(self.solution.part_1(), 3)

        with patch.object(Year2015Day01, "inputs", "(()(()("):
            self.assertEqual(self.solution.part_1(), 3)

        with patch.object(Year2015Day01, "inputs", "))((((("):
            self.assertEqual(self.solution.part_1(), 3)

        with patch.object(Year2015Day01, "inputs", "())"):
            self.assertEqual(self.solution.part_1(), -1)

        with patch.object(Year2015Day01, "inputs", "))("):
            self.assertEqual(self.solution.part_1(), -1)

        with patch.object(Year2015Day01, "inputs", ")))"):
            self.assertEqual(self.solution.part_1(), -3)

        with patch.object(Year2015Day01, "inputs", ")())())"):
            self.assertEqual(self.solution.part_1(), -3)

    def test_part_2(self):
        with patch.object(Year2015Day01, "inputs", ")"):
            self.assertEqual(self.solution.part_2(), 1)

        with patch.object(Year2015Day01, "inputs", "()())"):
            self.assertEqual(self.solution.part_2(), 5)
