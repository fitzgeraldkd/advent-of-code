from unittest.mock import patch

from solutions import BaseTestCase
from solutions.year_2016.day_07.solution import Year2016Day07


class TestSolution(BaseTestCase):
    def setUp(self):
        self.solution = Year2016Day07()
        self.answers = (110, 242)


class TestSample(BaseTestCase):
    def setUp(self):
        self.solution = Year2016Day07("sample.txt")
        self.answers = (None, None)

    def test_part_1(self):
        with patch.object(
            Year2016Day07,
            "inputs",
            [
                "abba[mnop]qrst",
                "abcd[bddb]xyyx",
                "aaaa[qwer]tyui",
                "ioxxoj[asdfgh]zxcvbn",
            ],
        ):
            self.assertEqual(self.solution.part_1(), 2)

    def test_part_2(self):
        with patch.object(
            Year2016Day07,
            "inputs",
            ["aba[bab]xyz", "xyx[xyx]xyx", "aaa[kek]eke", "zazbz[bzb]cdb"],
        ):
            self.assertEqual(self.solution.part_2(), 3)
