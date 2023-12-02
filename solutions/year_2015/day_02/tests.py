from unittest.mock import patch

from solutions import BaseTestCase
from solutions.year_2015.day_02.solution import Year2015Day02


class TestSolution(BaseTestCase):
    def setUp(self):
        self.solution = Year2015Day02()
        self.answers = (1588178, 3783758)


class TestSample(BaseTestCase):
    def setUp(self):
        self.solution = Year2015Day02()

    def test_part_1(self):
        with patch.object(Year2015Day02, "inputs", [[2, 3, 4]]):
            self.assertEqual(self.solution.part_1(), 58)

        with patch.object(Year2015Day02, "inputs", [[1, 1, 10]]):
            self.assertEqual(self.solution.part_1(), 43)

        with patch.object(Year2015Day02, "inputs", [[2, 3, 4], [1, 1, 10]]):
            self.assertEqual(self.solution.part_1(), 101)

    def test_part_2(self):
        with patch.object(Year2015Day02, "inputs", [[2, 3, 4]]):
            self.assertEqual(self.solution.part_2(), 34)

        with patch.object(Year2015Day02, "inputs", [[1, 1, 10]]):
            self.assertEqual(self.solution.part_2(), 14)

        with patch.object(Year2015Day02, "inputs", [[2, 3, 4], [1, 1, 10]]):
            self.assertEqual(self.solution.part_2(), 48)
