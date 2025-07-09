import unittest

from python.constants import MIN_QUALITY
from python.gilded_rose import Standard, Item

class StandardTest(unittest.TestCase):
    def test_item_is_updated(self):
        # arrange the test
        item = Standard(Item("Standard Item", 10, 20))
        expected_sell_in = 9
        expected_quality = 19
        # act
        item.update()
        # assert
        self.assertEqual(expected_sell_in, item.item.sell_in)
        self.assertEqual(expected_quality, item.item.quality)

    def test_item_quality_does_not_go_below_min_quantity(self):
        # arrange the test
        item = Standard(Item("Standard Item", 10, 0))
        expected_sell_in = 9
        expected_quality = MIN_QUALITY
        # act
        item.update()
        # assert
        self.assertEqual(expected_sell_in, item.item.sell_in)
        self.assertEqual(expected_quality, item.item.quality)

    def test_item_quality_decreases_twice_as_fast_after_sell_in(self):
        # arrange the test
        item = Standard(Item("Standard Item", 0, 20))
        expected_sell_in = -1
        expected_quality = 18
        # act
        item.update()
        # assert
        self.assertEqual(expected_sell_in, item.item.sell_in)
        self.assertEqual(expected_quality, item.item.quality)

if __name__ == '__main__':
    unittest.main()
