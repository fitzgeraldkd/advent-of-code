from solutions import BaseTestCase
from solutions.year_20XX.day_YY.solution import Year20XXDayYY


class TestSolution(BaseTestCase):
    def setUp(self):
        self.solution = Year20XXDayYY(__file__)
        self.answers = (None, None)


class TestSample(BaseTestCase):
    def setUp(self):
        self.solution = Year20XXDayYY(__file__, "sample.txt")
        self.answers = (None, None)
