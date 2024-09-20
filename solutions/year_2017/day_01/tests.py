from unittest.mock import patch

from solutions import BaseTestCase
from solutions.year_2017.day_01.solution import Year2017Day01


class TestSolution(BaseTestCase):
    def setUp(self):
        self.solution = Year2017Day01()
        self.answers = (1097, 1188)


class TestSample(BaseTestCase):
    def setUp(self):
        self.solution = Year2017Day01()    

    def test_part_1(self):
        with patch.object(Year2017Day01, 'inputs', '1122'):
            self.assertEqual(self.solution.part_1(), 3)
        with patch.object(Year2017Day01, 'inputs', '1111'):
            self.assertEqual(self.solution.part_1(), 4)
        with patch.object(Year2017Day01, 'inputs', '1234'):
            self.assertEqual(self.solution.part_1(), 0)
        with patch.object(Year2017Day01, 'inputs', '91212129'):
            self.assertEqual(self.solution.part_1(), 9)

    def test_part_2(self):
        with patch.object(Year2017Day01, 'inputs', '1212'):
            self.assertEqual(self.solution.part_2(), 6)
        with patch.object(Year2017Day01, 'inputs', '1221'):
            self.assertEqual(self.solution.part_2(), 0)
        with patch.object(Year2017Day01, 'inputs', '123425'):
            self.assertEqual(self.solution.part_2(), 4)
        with patch.object(Year2017Day01, 'inputs', '123123'):
            self.assertEqual(self.solution.part_2(), 12)
        with patch.object(Year2017Day01, 'inputs', '12131415'):
            self.assertEqual(self.solution.part_2(), 4)
