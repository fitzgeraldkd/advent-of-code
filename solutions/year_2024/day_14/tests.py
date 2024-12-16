from unittest.mock import patch
from solutions import BaseTestCase
from solutions.year_2024.day_14.solution import Year2024Day14


class TestSolution(BaseTestCase):
    def setUp(self):
        self.solution = Year2024Day14()
        self.answers = (230686500, None)


class TestSample(BaseTestCase):
    def setUp(self):
        self.solution = Year2024Day14("sample.txt")
        self.answers = (12, None)

    def test_part_1(self):
        with patch.object(Year2024Day14, "WIDTH", 11), patch.object(Year2024Day14, "HEIGHT", 7):
            return super().test_part_1()
