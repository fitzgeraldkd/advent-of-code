from unittest.mock import patch

from solutions import BaseTestCase
from solutions.year_2017.day_02.solution import Year2017Day02


class TestSolution(BaseTestCase):
    def setUp(self):
        self.solution = Year2017Day02()
        self.answers = (42378, 246)


class TestSample(BaseTestCase):
    def setUp(self):
        self.solution = Year2017Day02()
    
    def test_part_1(self):
        example_spreadsheet = [
            [5, 1, 9, 5],
            [7, 5, 3],
            [2, 4, 6, 8]
        ]
        with patch.object(Year2017Day02, "inputs", example_spreadsheet):
            self.assertEqual(self.solution.part_1(), 18)
    
    def test_part_2(self):
        example_spreadsheet = [
            [5, 9, 2, 8],
            [9, 4, 7, 3],
            [3, 8, 6, 5]
        ]
        with patch.object(Year2017Day02, "inputs", example_spreadsheet):
            self.assertEqual(self.solution.part_2(), 9)

