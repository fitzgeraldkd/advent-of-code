from unittest.mock import ANY, patch

from solutions import BaseTestCase
from solutions.year_2016.day_16.solution import Year2016Day16


class TestSolution(BaseTestCase):
    def setUp(self):
        self.solution = Year2016Day16()
        self.answers = ("11111000111110000", "10111100110110100")


class TestSample(BaseTestCase):
    def setUp(self):
        self.solution = Year2016Day16("sample.txt")
        self.answers = ("01100", ANY)

    @patch.object(Year2016Day16, "PART_1_LENGTH", 20)
    def test_part_1(self):
        return super().test_part_1()
