from solutions import BaseTestCase
from solutions.year_2020.day_19.solution import Year2020Day19


class TestSolution(BaseTestCase):
    def setUp(self):
        self.solution = Year2020Day19()
        self.answers = (208, 316)


class TestSample1(BaseTestCase):
    def setUp(self):
        self.solution = Year2020Day19("sample1.txt")
        self.answers = (2, None)

    def test_part_2(self):
        pass


class TestSample2(BaseTestCase):
    def setUp(self):
        self.solution = Year2020Day19("sample2.txt")
        self.answers = (3, 12)
