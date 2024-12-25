from solutions import BaseTestCase
from solutions.year_2024.day_22.solution import Year2024Day22


class TestSolution(BaseTestCase):
    def setUp(self):
        self.solution = Year2024Day22()
        self.answers = (19822877190, 2277)


class TestSample(BaseTestCase):
    def setUp(self):
        self.answers = (37327623, 23)

    def test_part_1(self):
        self.solution = Year2024Day22("sample1.txt")
        return super().test_part_1()

    def test_part_2(self):
        self.solution = Year2024Day22("sample2.txt")
        return super().test_part_2()
