from unittest.mock import patch

from solutions import BaseTestCase
from solutions.year_2017.day_09.solution import Year2017Day09


class TestSolution(BaseTestCase):
    def setUp(self):
        self.solution = Year2017Day09()
        self.answers = (16827, 7298)


class TestSample(BaseTestCase):
    def setUp(self):
        self.solution = Year2017Day09("sample.txt")

    def test_part_1(self):
        test_cases = [
            ('{}', 1),
            ('{{{}}}', 6),
            ('{{},{}}', 5),
            ('{{{},{},{{}}}}', 16),
            ('{<a>,<a>,<a>,<a>}', 1),
            ('{{<ab>},{<ab>},{<ab>},{<ab>}}', 9),
            ('{{<!!>},{<!!>},{<!!>},{<!!>}}', 9),
            ('{{<a!>},{<a!>},{<a!>},{<ab>}}', 3),
        ]

        for input, output in test_cases:
            with patch.object(Year2017Day09, "inputs", input):
                self.assertEqual(self.solution.part_1(), output)

    def test_part_2(self):
        test_cases = [
            ('<>', 0),
            ('<random characters>', 17),
            ('<<<<>', 3),
            ('<{!>}>', 2),
            ('<!!>', 0),
            ('<!!!>>', 0),
            ('<{o"i!a,<{i<a>', 10),
        ]

        for input, output in test_cases:
            with patch.object(Year2017Day09, "inputs", input):
                self.assertEqual(self.solution.part_2(), output)


    # def test_part_1(self):
    #     self.assertEqual(part_1('{}'), 1)
    #     self.assertEqual(part_1('{{{}}}'), 6)
    #     self.assertEqual(part_1('{{},{}}'), 5)
    #     self.assertEqual(part_1('{{{},{},{{}}}}'), 16)
    #     self.assertEqual(part_1('{<a>,<a>,<a>,<a>}'), 1)
    #     self.assertEqual(part_1('{{<ab>},{<ab>},{<ab>},{<ab>}}'), 9)
    #     self.assertEqual(part_1('{{<!!>},{<!!>},{<!!>},{<!!>}}'), 9)
    #     self.assertEqual(part_1('{{<a!>},{<a!>},{<a!>},{<ab>}}'), 3)

    # def test_part_2(self):
    #     self.assertEqual(part_2('<>'), 0)
    #     self.assertEqual(part_2('<random characters>'), 17)
    #     self.assertEqual(part_2('<<<<>'), 3)
    #     self.assertEqual(part_2('<{!>}>'), 2)
    #     self.assertEqual(part_2('<!!>'), 0)
    #     self.assertEqual(part_2('<!!!>>'), 0)
    #     self.assertEqual(part_2('<{o"i!a,<{i<a>'), 10)