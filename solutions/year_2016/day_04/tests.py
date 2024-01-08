from solutions import BaseTestCase
from solutions.year_2016.day_04.solution import Year2016Day04


class TestSolution(BaseTestCase):
    def setUp(self):
        self.solution = Year2016Day04()
        self.answers = (278221, 267)
