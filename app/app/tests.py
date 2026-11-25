""" Sample Tests. """

from django.test import SimpleTestCase

from app import calc


class CalcTests(SimpleTestCase):
    """ Test the calc module. """

    def test_add_numbers(self):
        """ Test adding 2 numbers together. """
        res = calc.add_two_nums(5, 6)
        self.assertEqual(res, 11)

    def test_sub_numbers(self):
        """ Test subtracting 2 numbers. """
        res = calc.sub_two_nums(27, 9)
        self.assertEqual(res, 18)
