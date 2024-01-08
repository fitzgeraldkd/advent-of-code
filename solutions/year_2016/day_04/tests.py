from unittest import TestCase
from unittest.mock import patch

from solutions import BaseTestCase
from solutions.year_2016.day_04.solution import Year2016Day04


class TestSolution(BaseTestCase):
    def setUp(self):
        self.solution = Year2016Day04()
        self.answers = (278221, 267)

class TestSample(BaseTestCase):
    def setUp(self):
        self.solution = Year2016Day04()

    def test_part_1(self):
        with patch.object(Year2016Day04, '_read_inputs', return_value=[
            'aaaaa-bbb-z-y-x-123[abxyz]',
            'a-b-c-d-e-f-g-h-987[abcde]',
            'not-a-real-room-404[oarel]',
            'totally-real-room-200[decoy]',
        ]):
            self.assertEqual(self.solution.part_1(), 1514)

    def test_part_2(self):
        pass


class TestUtils(TestCase):
    def test_decrypt_room_name(self):
        solution = Year2016Day04()
        self.assertEqual(solution.decrypt_room_name('qzmt zixmtkozy ivhz', 343), 'very encrypted name')
