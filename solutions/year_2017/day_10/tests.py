from unittest.mock import patch

from solutions import BaseTestCase
from solutions.year_2017.day_10.solution import Year2017Day10


class TestSolution(BaseTestCase):
    def setUp(self):
        self.solution = Year2017Day10()
        self.answers = (4480, 'c500ffe015c83b60fad2e4b7d59dabc4')


class TestSample(BaseTestCase):
    def setUp(self):
        self.solution = Year2017Day10("sample.txt")
        self.answers = (None, None)

    def test_part_1(self):
        with patch.object(Year2017Day10, "LENGTH", 5), patch.object(Year2017Day10, "inputs", "3,4,1,5"):
            self.assertEqual(self.solution.part_1(), 12)

    def test_part_2(self):
        test_cases = [
            ("", "a2582a3a0e66e6e86e3812dcb672a272"),
            ("AoC 2017", "33efeb34ea91902bb2f59c9920caa6cd"),
            ("1,2,3", "3efbe78a8d82f29979031a4aa0b16a9d"),
            ("1,2,4", "63960835bcdc130f0b66d7ff4f6a5a8e"),
        ]

        for input, output in test_cases:
            with patch.object(Year2017Day10, "inputs", input):
                self.assertEqual(self.solution.part_2(), output)
