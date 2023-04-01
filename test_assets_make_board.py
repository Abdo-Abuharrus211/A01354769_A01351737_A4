
from unittest import TestCase
# from unittest.mock import patch

from assets import make_board


class TestMakeBoard(TestCase):

    def test_make_board_type_error_row(self):
        with self.assertRaises(ValueError):
            rows = 8
            columns = 10
            make_board(rows, columns)

    def test_make_board_type_error_column(self):
        with self.assertRaises(ValueError):
            rows = 2
            columns = 10
            make_board(rows, columns)


