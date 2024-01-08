from solutions import BaseTestCase
from solutions.year_2015.day_23.solution import Year2015Day23


class TestSolution(BaseTestCase):
    def setUp(self):
        self.solution = Year2015Day23()
        self.answers = (170, 247)
