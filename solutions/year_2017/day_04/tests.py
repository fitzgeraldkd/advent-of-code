from unittest.mock import patch

from solutions import BaseTestCase
from solutions.year_2017.day_04.solution import Year2017Day04


class TestSolution(BaseTestCase):
    def setUp(self):
        self.solution = Year2017Day04()
        self.answers = (466, 251)


class TestSample(BaseTestCase):
    def setUp(self):
        self.solution = Year2017Day04("sample.txt")
        self.answers = (2, 3)

    def test_part_1(self):
        sample_passphrases = [
            "aa bb cc dd ee",
            "aa bb cc dd aa",
            "aa bb cc dd aaa"
        ]
        with patch.object(Year2017Day04, "_read_inputs", return_value=sample_passphrases):
            return super().test_part_1()

    def test_part_2(self):
        sample_passphrases = [
            "abcde fghij",
            "abcde xyz ecdab",
            "a ab abc abd abf abj",
            "iiii oiii ooii oooi oooo",
            "oiii ioii iioi iiio"
        ]
        with patch.object(Year2017Day04, "_read_inputs", return_value=sample_passphrases):
            return super().test_part_2()
