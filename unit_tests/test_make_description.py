
from unittest import TestCase
from unittest.mock import patch

from assets import make_description


class TestMakeDescription(TestCase):

    @patch('random.randint', side_effect=[4])
    def test_make_description_4(self, _):
        actual_output = make_description()
        self.assertEqual(actual_output,  "The room is filled with the rich scent of old leather bindings"
                                         " and musty pages, mingling with the faint aroma of brewing coffee and "
                                         "the sweet scent of sugary treats.")

    @patch('random.randint', side_effect=[0])
    def test_make_description_15(self, _):
        actual_output = make_description()
        self.assertEqual(actual_output, "The dusty scrolls of the stacks howled with an eerie silence")
