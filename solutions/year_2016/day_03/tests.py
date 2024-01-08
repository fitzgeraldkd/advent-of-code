from solutions import BaseTestCase
from solutions.year_2016.day_03.solution import Year2016Day03


class TestSolution(BaseTestCase):
    def setUp(self):
        self.solution = Year2016Day03()
        self.answers = (869, 1544)
