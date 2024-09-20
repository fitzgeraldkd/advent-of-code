from unittest.mock import patch

from solutions import BaseTestCase
from solutions.year_2017.day_03.solution import Year2017Day03


class TestSolution(BaseTestCase):
    def setUp(self):
        self.solution = Year2017Day03()
        self.answers = (419, 295229)


class TestSample(BaseTestCase):
    def setUp(self):
        self.solution = Year2017Day03()
    
    def test_part_1(self):
        with patch.object(Year2017Day03, "inputs", 1):
            self.assertEqual(self.solution.part_1(), 0)
        with patch.object(Year2017Day03, "inputs", 12):
            self.assertEqual(self.solution.part_1(), 3)
        with patch.object(Year2017Day03, "inputs", 23):
            self.assertEqual(self.solution.part_1(), 2)
        with patch.object(Year2017Day03, "inputs", 1024):
            self.assertEqual(self.solution.part_1(), 31)
        # self.assertEqual(part_1(1), 0)
        # self.assertEqual(part_1(12), 3)
        # self.assertEqual(part_1(23), 2)
        # self.assertEqual(part_1(1024), 31)
    
    def test_part_2(self):
        pass
