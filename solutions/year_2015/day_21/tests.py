from solutions import BaseTestCase
from solutions.year_2015.day_21.solution import Year2015Day21


class TestSolution(BaseTestCase):
    def setUp(self):
        self.solution = Year2015Day21()
        self.answers = (111, 188)
