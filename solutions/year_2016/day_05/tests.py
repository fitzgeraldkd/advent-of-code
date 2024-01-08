from solutions import BaseTestCase
from solutions.year_2016.day_05.solution import Year2016Day05


class TestSolution(BaseTestCase):
    def setUp(self):
        self.solution = Year2016Day05()
        self.answers = ('f97c354d', '863dde27')
