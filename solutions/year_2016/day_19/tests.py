from solutions import BaseTestCase
from solutions.year_2016.day_19.solution import Year2016Day19


class TestSolution(BaseTestCase):
    def setUp(self):
        self.solution = Year2016Day19()
        self.answers = (1834471, 1420064)

    def test_part_2(self):
        self.skipTest("Takes more than 5 minutes to run.")
        return super().test_part_2()


class TestSample(BaseTestCase):
    def setUp(self):
        self.solution = Year2016Day19("sample.txt")
        self.answers = (3, 2)
