from solutions import BaseTestCase
from solutions.year_2024.day_23.solution import Year2024Day23


class TestSolution(BaseTestCase):
    def setUp(self):
        self.solution = Year2024Day23()
        self.answers = (1348, "am,bv,ea,gh,is,iy,ml,nj,nl,no,om,tj,yv")


class TestSample(BaseTestCase):
    def setUp(self):
        self.solution = Year2024Day23("sample.txt")
        self.answers = (7, "co,de,ka,ta")
