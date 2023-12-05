from solutions import BaseTestCase
from solutions.year_2023.day_05.solution import Year2023Day05


class TestSolution(BaseTestCase):
    def setUp(self):
        self.solution = Year2023Day05()
        self.answers = (993500720, 4917124)


class TestSample(BaseTestCase):
    def setUp(self):
        self.solution = Year2023Day05("sample.txt")
        self.answers = (35, 46)
