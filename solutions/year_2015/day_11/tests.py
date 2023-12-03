from unittest import TestCase
from unittest.mock import patch

from solutions import BaseTestCase
from solutions.year_2015.day_11.solution import Year2015Day11


class TestSolution(BaseTestCase):
    def setUp(self):
        self.solution = Year2015Day11()
        self.answers = ("cqjxxyzz", "cqkaabcc")


class TestSample(BaseTestCase):
    def setUp(self):
        self.solution = Year2015Day11()

    def test_part_1(self):
        with patch.object(Year2015Day11, "inputs", "abcdefgh"):
            self.assertEqual(self.solution.part_1(), "abcdffaa")

        with patch.object(Year2015Day11, "inputs", "ghijklmn"):
            self.assertEqual(self.solution.part_1(), "ghjaabcc")

    def test_part_2(self):
        pass


class TestUtils(TestCase):
    def test_passes_rules(self):
        solution = Year2015Day11()
        self.assertFalse(solution.passes_rules("hijklmmn"))
        self.assertFalse(solution.passes_rules("abbceffg"))
        self.assertFalse(solution.passes_rules("abbcegjk"))
        self.assertTrue(solution.passes_rules("abcdffaa"))
        self.assertTrue(solution.passes_rules("ghjaabcc"))
