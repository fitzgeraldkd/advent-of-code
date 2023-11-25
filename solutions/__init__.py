import os
import unittest
from typing import Any, Tuple


class BaseSolution:
    def __init__(self, file: str, inputs_filename="inputs.txt"):
        self.inputs_path = os.path.join(os.path.dirname(file), inputs_filename)

    def _parse_line(self, line: str):
        return line.strip()

    def _parse_inputs(self):
        return [self._parse_line(line) for line in self._read_inputs()]

    def _read_inputs(self):
        with open(self.inputs_path) as inputs:
            lines = inputs.readlines()

        return lines

    @property
    def inputs(self):
        return self._parse_inputs()

    def part_1(self):
        return None

    def part_2(self):
        return None

    def print_results(self):
        print("Part 1:", self.part_1())
        print("Part 2:", self.part_2())


class BaseTestCase(unittest.TestCase):
    def setUp(self):
        self.solution = BaseSolution(__file__)
        self.answers: Tuple[Any, Any] = (None, None)

    def test_part_1(self):
        self.assertEqual(self.solution.part_1(), self.answers[0])

    def test_part_2(self):
        self.assertEqual(self.solution.part_2(), self.answers[1])
