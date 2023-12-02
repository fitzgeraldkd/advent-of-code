from unittest.mock import patch

from solutions import BaseTestCase
from solutions.year_2015.day_04.solution import Year2015Day04


class TestSolution(BaseTestCase):
    def setUp(self):
        self.solution = Year2015Day04()
        self.answers = (254575, 1038736)


class TestSample(BaseTestCase):
    def setUp(self):
        self.solution = Year2015Day04()

    def test_part_1(self):
        with patch.object(Year2015Day04, "inputs", "abcdef"):
            self.assertEqual(self.solution.part_1(), 609043)

        with patch.object(Year2015Day04, "inputs", "pqrstuv"):
            self.assertEqual(self.solution.part_1(), 1048970)

    def test_part_2(self):
        pass
