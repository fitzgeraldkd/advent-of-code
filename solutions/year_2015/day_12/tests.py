from unittest.mock import patch

from solutions import BaseTestCase
from solutions.year_2015.day_12.solution import Year2015Day12


class TestSolution(BaseTestCase):
    def setUp(self):
        self.solution = Year2015Day12()
        self.answers = (119433, 68466)


class TestSample(BaseTestCase):
    def setUp(self):
        self.solution = Year2015Day12()

    def test_part_1(self):
        with patch.object(Year2015Day12, "inputs", "[1,2,3]"):
            self.assertEqual(self.solution.part_1(), 6)
        with patch.object(Year2015Day12, "inputs", '{"a":2,"b":4}'):
            self.assertEqual(self.solution.part_1(), 6)
        with patch.object(Year2015Day12, "inputs", "[[[3]]]"):
            self.assertEqual(self.solution.part_1(), 3)
        with patch.object(Year2015Day12, "inputs", '{"a":{"b":4},"c":-1}'):
            self.assertEqual(self.solution.part_1(), 3)
        with patch.object(Year2015Day12, "inputs", '{"a":[-1,1]}'):
            self.assertEqual(self.solution.part_1(), 0)
        with patch.object(Year2015Day12, "inputs", '[-1,{"a":1}]'):
            self.assertEqual(self.solution.part_1(), 0)
        with patch.object(Year2015Day12, "inputs", "[]"):
            self.assertEqual(self.solution.part_1(), 0)
        with patch.object(Year2015Day12, "inputs", "{}"):
            self.assertEqual(self.solution.part_1(), 0)

    def test_part_2(self):
        with patch.object(Year2015Day12, "inputs", "[1,2,3]"):
            self.assertEqual(self.solution.part_2(), 6)
        with patch.object(Year2015Day12, "inputs", '[1,{"c":"red","b":2},3]'):
            self.assertEqual(self.solution.part_2(), 4)
        with patch.object(Year2015Day12, "inputs", '{"d":"red","e":[1,2,3,4],"f":5}'):
            self.assertEqual(self.solution.part_2(), 0)
        with patch.object(Year2015Day12, "inputs", '[1,"red",5]'):
            self.assertEqual(self.solution.part_2(), 6)
