from unittest.mock import patch

from solutions import BaseTestCase
from solutions.year_2020.day_15.solution import Year2020Day15


class TestSolution(BaseTestCase):
    def setUp(self):
        self.solution = Year2020Day15()
        self.answers = (614, 1065)


class TestSample(BaseTestCase):
    def setUp(self):
        self.solution = Year2020Day15()

    def test_part_1(self):
        with patch.object(Year2020Day15, "_read_inputs", return_value=["0,3,6"]):
            self.assertEqual(self.solution.part_1(), 436)
        with patch.object(Year2020Day15, "_read_inputs", return_value=["1,3,2"]):
            self.assertEqual(self.solution.part_1(), 1)
        with patch.object(Year2020Day15, "_read_inputs", return_value=["2,1,3"]):
            self.assertEqual(self.solution.part_1(), 10)
        with patch.object(Year2020Day15, "_read_inputs", return_value=["1,2,3"]):
            self.assertEqual(self.solution.part_1(), 27)
        with patch.object(Year2020Day15, "_read_inputs", return_value=["2,3,1"]):
            self.assertEqual(self.solution.part_1(), 78)
        with patch.object(Year2020Day15, "_read_inputs", return_value=["3,2,1"]):
            self.assertEqual(self.solution.part_1(), 438)
        with patch.object(Year2020Day15, "_read_inputs", return_value=["3,1,2"]):
            self.assertEqual(self.solution.part_1(), 1836)

    def test_part_2(self):
        with patch.object(Year2020Day15, "_read_inputs", return_value=["0,3,6"]):
            self.assertEqual(self.solution.part_2(), 175594)
        with patch.object(Year2020Day15, "_read_inputs", return_value=["1,3,2"]):
            self.assertEqual(self.solution.part_2(), 2578)
        with patch.object(Year2020Day15, "_read_inputs", return_value=["2,1,3"]):
            self.assertEqual(self.solution.part_2(), 3544142)
        with patch.object(Year2020Day15, "_read_inputs", return_value=["1,2,3"]):
            self.assertEqual(self.solution.part_2(), 261214)
        with patch.object(Year2020Day15, "_read_inputs", return_value=["2,3,1"]):
            self.assertEqual(self.solution.part_2(), 6895259)
        with patch.object(Year2020Day15, "_read_inputs", return_value=["3,2,1"]):
            self.assertEqual(self.solution.part_2(), 18)
        with patch.object(Year2020Day15, "_read_inputs", return_value=["3,1,2"]):
            self.assertEqual(self.solution.part_2(), 362)
