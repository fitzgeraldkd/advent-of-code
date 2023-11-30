from unittest.mock import patch

from solutions import BaseTestCase
from solutions.year_2020.day_05.solution import Year2020Day05


class TestSolution(BaseTestCase):
    def setUp(self):
        self.solution = Year2020Day05(__file__)
        self.answers = (976, 685)


class TestSample(BaseTestCase):
    def setUp(self):
        self.solution = Year2020Day05(__file__, "sample.txt")

    def test_part_1(self):
        self.assertListEqual(self.solution.inputs, [357, 567, 119, 820])
        self.assertEqual(self.solution.part_1(), 820)

    def test_part_2(self):
        pass
