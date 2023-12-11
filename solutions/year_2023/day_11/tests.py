from unittest.mock import ANY, patch

from solutions import BaseTestCase
from solutions.year_2023.day_11.solution import Year2023Day11


class TestSolution(BaseTestCase):
    def setUp(self):
        self.solution = Year2023Day11()
        self.answers = (9605127, 458191688761)


class TestSample(BaseTestCase):
    def setUp(self):
        self.solution = Year2023Day11("sample.txt")
        self.answers = (374, ANY)

    def test_part_2(self):
        with patch.object(Year2023Day11, "PART_2_EXPANSION_FACTOR", 10):
            self.assertEqual(self.solution.part_2(), 1030)

        with patch.object(Year2023Day11, "PART_2_EXPANSION_FACTOR", 100):
            self.assertEqual(self.solution.part_2(), 8410)
