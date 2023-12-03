from unittest.mock import ANY

from solutions import BaseTestCase
from solutions.year_2020.day_16.solution import Year2020Day16


class TestSolution(BaseTestCase):
    def setUp(self):
        self.solution = Year2020Day16()
        self.answers = (18227, 2355350878831)


class TestSample1(BaseTestCase):
    def setUp(self):
        self.solution = Year2020Day16("sample1.txt")
        self.answers = (71, ANY)

    def test_part_2(self):
        pass


class TestSample2(BaseTestCase):
    def setUp(self):
        self.solution = Year2020Day16("sample2.txt")
        self.answers = (ANY, ANY)

    def test_part_2(self):
        fields, my_ticket, other_tickets = self.solution.inputs
        valid_tickets = [my_ticket, *other_tickets]
        self.assertDictEqual(
            self.solution.identify_fields(fields, valid_tickets),
            {
                "class": 1,
                "row": 0,
                "seat": 2,
            },
        )
