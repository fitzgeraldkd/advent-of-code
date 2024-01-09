from unittest import TestCase

from solutions import BaseTestCase
from solutions.year_2016.day_09.solution import Year2016Day09


class TestSolution(BaseTestCase):
    def setUp(self):
        self.solution = Year2016Day09()
        self.answers = (115118, 11107527530)


class TestUtils(TestCase):
    def test_decompress(self):
        solution = Year2016Day09()
        self.assertEqual(solution.decompress("ADVENT"), "ADVENT")
        self.assertEqual(solution.decompress("A(1x5)BC"), "ABBBBBC")
        self.assertEqual(solution.decompress("(3x3)XYZ"), "XYZXYZXYZ")
        self.assertEqual(solution.decompress("A(2x2)BCD(2x2)EFG"), "ABCBCDEFEFG")
        self.assertEqual(solution.decompress("(6x1)(1x3)A"), "(1x3)A")
        self.assertEqual(solution.decompress("X(8x2)(3x3)ABCY"), "X(3x3)ABC(3x3)ABCY")

    def test_decompress_recursive(self):
        solution = Year2016Day09()
        self.assertEqual(solution.decompress_recursive("(3x3)XYZ"), 9)
        self.assertEqual(solution.decompress_recursive("X(8x2)(3x3)ABCY"), 20)
        self.assertEqual(
            solution.decompress_recursive("(27x12)(20x12)(13x14)(7x10)(1x12)A"), 241920
        )
        self.assertEqual(
            solution.decompress_recursive(
                "(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN"
            ),
            445,
        )
