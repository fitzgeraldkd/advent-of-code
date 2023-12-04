from solutions import BaseTestCase
from solutions.year_2015.day_16.solution import Year2015Day16


class TestSolution(BaseTestCase):
    def setUp(self):
        self.solution = Year2015Day16()
        self.answers = (103, 405)
