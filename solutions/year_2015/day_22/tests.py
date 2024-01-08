from solutions import BaseTestCase
from solutions.year_2015.day_22.solution import Year2015Day22


class TestSolution(BaseTestCase):
    def setUp(self):
        self.solution = Year2015Day22()
        self.answers = (900, 1216)
