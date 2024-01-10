from solutions import BaseTestCase
from solutions.year_2016.day_25.solution import Year2016Day25


class TestSolution(BaseTestCase):
    def setUp(self):
        self.solution = Year2016Day25()
        self.answers = (196, None)
