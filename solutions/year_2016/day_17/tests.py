from unittest.mock import patch

from solutions import BaseTestCase
from solutions.year_2016.day_17.solution import Year2016Day17


class TestSolution(BaseTestCase):
    def setUp(self):
        self.solution = Year2016Day17()
        self.answers = ("DDURRLRRDD", 436)


class TestSample(BaseTestCase):
    def setUp(self):
        self.solution = Year2016Day17()

    def test_part_1(self):
        with patch.object(Year2016Day17, "inputs", "ihgpwlah"):
            self.assertEqual(self.solution.part_1(), "DDRRRD")
        with patch.object(Year2016Day17, "inputs", "kglvqrro"):
            self.assertEqual(self.solution.part_1(), "DDUDRLRRUDRD")
        with patch.object(Year2016Day17, "inputs", "ulqzkmiv"):
            self.assertEqual(self.solution.part_1(), "DRURDRUDDLLDLUURRDULRLDUUDDDRR")

    def test_part_2(self):
        with patch.object(Year2016Day17, "inputs", "ihgpwlah"):
            self.assertEqual(self.solution.part_2(), 370)
        with patch.object(Year2016Day17, "inputs", "kglvqrro"):
            self.assertEqual(self.solution.part_2(), 492)
        with patch.object(Year2016Day17, "inputs", "ulqzkmiv"):
            self.assertEqual(self.solution.part_2(), 830)
