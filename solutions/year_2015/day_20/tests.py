from unittest.mock import patch

from solutions import BaseTestCase
from solutions.year_2015.day_20.solution import Year2015Day20


class TestSolution(BaseTestCase):
    def setUp(self):
        self.solution = Year2015Day20()
        self.answers = (776160, 786240)


class TestSample(BaseTestCase):
    def setUp(self):
        self.solution = Year2015Day20()

    def test_part_1(self):
        with patch.object(Year2015Day20, "inputs", 10):
            self.assertEqual(self.solution.part_1(), 1)
        with patch.object(Year2015Day20, "inputs", 30):
            self.assertEqual(self.solution.part_1(), 2)
        with patch.object(Year2015Day20, "inputs", 40):
            self.assertEqual(self.solution.part_1(), 3)
        with patch.object(Year2015Day20, "inputs", 60):
            self.assertEqual(self.solution.part_1(), 4)
        with patch.object(Year2015Day20, "inputs", 70):
            self.assertEqual(self.solution.part_1(), 4)
        with patch.object(Year2015Day20, "inputs", 80):
            self.assertEqual(self.solution.part_1(), 6)
        with patch.object(Year2015Day20, "inputs", 120):
            self.assertEqual(self.solution.part_1(), 6)
        with patch.object(Year2015Day20, "inputs", 130):
            self.assertEqual(self.solution.part_1(), 8)
        with patch.object(Year2015Day20, "inputs", 150):
            self.assertEqual(self.solution.part_1(), 8)

    def test_part_2(self):
        pass
