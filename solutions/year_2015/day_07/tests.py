from unittest.mock import patch

from solutions import BaseTestCase
from solutions.year_2015.day_07.solution import Year2015Day07


class TestSolution(BaseTestCase):
    def setUp(self):
        self.solution = Year2015Day07(__file__)
        self.answers = (3176, 14710)


class TestSample(BaseTestCase):
    def setUp(self):
        self.solution = Year2015Day07(__file__, "sample.txt")

    def test_part_1(self):
        with patch("solutions.year_2015.day_07.solution.TARGET_WIRE", "d"):
            self.assertEqual(self.solution.part_1(), 72)
        with patch("solutions.year_2015.day_07.solution.TARGET_WIRE", "e"):
            self.assertEqual(self.solution.part_1(), 507)
        with patch("solutions.year_2015.day_07.solution.TARGET_WIRE", "f"):
            self.assertEqual(self.solution.part_1(), 492)
        with patch("solutions.year_2015.day_07.solution.TARGET_WIRE", "g"):
            self.assertEqual(self.solution.part_1(), 114)
        with patch("solutions.year_2015.day_07.solution.TARGET_WIRE", "h"):
            self.assertEqual(self.solution.part_1(), 65412)
        with patch("solutions.year_2015.day_07.solution.TARGET_WIRE", "i"):
            self.assertEqual(self.solution.part_1(), 65079)

    def test_part_2(self):
        pass
