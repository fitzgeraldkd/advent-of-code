import os
import unittest
from itertools import groupby
from typing import Any, List, Optional, Tuple


class BaseSolution:
    group_delimiter: Optional[str] = None
    module_file = __file__

    def __init__(self, inputs_filename="inputs.txt", module_file: str = None):
        self.inputs_filename = inputs_filename

        if module_file:
            self.module_file = module_file

    def _get_inputs_path(self):
        return os.path.join(os.path.dirname(self.module_file), self.inputs_filename)

    def _parse_line(self, line: str):
        """
        Parse a single line from the inputs text file.
        """
        return line.strip()

    def _parse_group(self, lines: List[str]):
        """
        Parse a group of lines. By default, this only gets applied if a group_delimiter
        is set.
        """
        return [self._parse_line(line) for line in lines]

    def _parse_inputs(self):
        """
        Parse the list of inputs provided from the text file.
        """
        if self.group_delimiter is None:
            return [self._parse_line(line) for line in self._read_inputs()]
        else:
            return [
                self._parse_group(list(group))
                for key, group in groupby(
                    self._read_inputs(), lambda line: line == self.group_delimiter
                )
                if not key
            ]

    def _read_inputs(self):
        """
        Read the inputs text file, without making any changes.
        """
        with open(self._get_inputs_path()) as inputs:
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
        self.solution = BaseSolution()
        self.answers: Tuple[Any, Any] = (None, None)

    def test_part_1(self):
        self.assertEqual(self.solution.part_1(), self.answers[0])

    def test_part_2(self):
        self.assertEqual(self.solution.part_2(), self.answers[1])
