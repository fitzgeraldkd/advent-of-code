from solutions import BaseTestCase
from solutions.year_2018.day_06.solution import Year2018Day06


class TestSolution(BaseTestCase):
    def setUp(self):
        self.solution = Year2018Day06()
        self.answers = (4771, 39149)


class TestSample(BaseTestCase):
    def setUp(self):
        self.solution = Year2018Day06("sample.txt")
        self.solution.PART_2_TARGET_DISTANCE = 32
        self.answers = (17, 16)
