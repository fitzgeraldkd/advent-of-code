from unittest.mock import patch

from solutions import BaseTestCase
from solutions.year_2016.day_01.solution import Year2016Day01


class TestSolution(BaseTestCase):
    def setUp(self):
        self.solution = Year2016Day01()
        self.answers = (242, 150)


class TestSample(BaseTestCase):
    def setUp(self):
        self.solution = Year2016Day01("sample.txt")
        self.answers = (None, None)

    def test_part_1(self):
        with patch.object(Year2016Day01, "inputs", ["R2", "L3"]):
            self.assertEqual(self.solution.part_1(), 5)
        with patch.object(Year2016Day01, "inputs", ["R2", "R2", "R2"]):
            self.assertEqual(self.solution.part_1(), 2)
        with patch.object(Year2016Day01, "inputs", ["R5", "L5", "R5", "R3"]):
            self.assertEqual(self.solution.part_1(), 12)

    def test_part_2(self):
        with patch.object(Year2016Day01, "inputs", ["R8", "R4", "R4", "R8"]):
            self.assertEqual(self.solution.part_2(), 4)
