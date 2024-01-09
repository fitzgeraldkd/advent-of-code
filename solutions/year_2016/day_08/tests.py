from unittest.mock import call, patch

from solutions import BaseTestCase
from solutions.year_2016.day_08.solution import Year2016Day08


class TestSolution(BaseTestCase):
    def setUp(self):
        self.solution = Year2016Day08()
        self.answers = (121, None)

    @patch("builtins.print")
    def test_part_2(self, mocked_print):
        super().test_part_2()
        self.assertEqual(mocked_print.call_count, 6)
        self.assertListEqual(
            mocked_print.call_args_list,
            [
                call("###..#..#.###..#..#..##..####..##..####..###.#...."),
                call("#..#.#..#.#..#.#..#.#..#.#....#..#.#......#..#...."),
                call("#..#.#..#.#..#.#..#.#....###..#..#.###....#..#...."),
                call("###..#..#.###..#..#.#....#....#..#.#......#..#...."),
                call("#.#..#..#.#.#..#..#.#..#.#....#..#.#......#..#...."),
                call("#..#..##..#..#..##...##..####..##..####..###.####."),
            ],
        )


class TestSample(BaseTestCase):
    def setUp(self):
        self.solution = Year2016Day08("sample.txt")
        self.answers = (6, None)

    @patch("builtins.print")
    def test_part_2(self, _mocked_print):
        return super().test_part_2()
