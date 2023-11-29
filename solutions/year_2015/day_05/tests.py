from unittest.mock import patch

from solutions import BaseTestCase
from solutions.year_2015.day_05.solution import Year2015Day05


class TestSolution(BaseTestCase):
    def setUp(self):
        self.solution = Year2015Day05(__file__)
        self.answers = (258, 53)


class TestSample(BaseTestCase):
    def setUp(self):
        self.solution = Year2015Day05(__file__)

    def test_part_1(self):
        with patch.object(Year2015Day05, "inputs", ["ugknbfddgicrmopn"]):
            self.assertEqual(self.solution.part_1(), 1)

        with patch.object(Year2015Day05, "inputs", ["aaa"]):
            self.assertEqual(self.solution.part_1(), 1)

        with patch.object(Year2015Day05, "inputs", ["jchzalrnumimnmhp"]):
            self.assertEqual(self.solution.part_1(), 0)

        with patch.object(Year2015Day05, "inputs", ["haegwjzuvuyypxyu"]):
            self.assertEqual(self.solution.part_1(), 0)

        with patch.object(Year2015Day05, "inputs", ["dvszwmarrgswjxmb"]):
            self.assertEqual(self.solution.part_1(), 0)

    def test_part_2(self):
        with patch.object(Year2015Day05, "inputs", ["qjhvhtzxzqqjkmpb"]):
            self.assertEqual(self.solution.part_2(), 1)

        with patch.object(Year2015Day05, "inputs", ["xxyxx"]):
            self.assertEqual(self.solution.part_2(), 1)

        with patch.object(Year2015Day05, "inputs", ["uurcxstgmygtbstg"]):
            self.assertEqual(self.solution.part_2(), 0)

        with patch.object(Year2015Day05, "inputs", ["ieodomkazucvgmuy"]):
            self.assertEqual(self.solution.part_2(), 0)
