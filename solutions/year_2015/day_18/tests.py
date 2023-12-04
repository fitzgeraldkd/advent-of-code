from solutions import BaseTestCase
from solutions.year_2015.day_18.solution import Year2015Day18


class TestSolution(BaseTestCase):
    def setUp(self):
        self.solution = Year2015Day18()
        self.answers = (814, 924)


class TestSample(BaseTestCase):
    def setUp(self):
        self.solution = Year2015Day18("sample.txt")
        self.answers = (4, 17)

    def test_part_1(self):
        self.solution.STEPS = 4
        return super().test_part_1()

    def test_part_2(self):
        self.solution.STEPS = 5
        return super().test_part_2()
