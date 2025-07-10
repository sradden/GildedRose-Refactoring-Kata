import unittest

from python.gilded_rose import Conjured, Item

class ConjuredTest(unittest.TestCase):
    def test_item_is_updated(self):
        # arrange the test
        item = Conjured(Item("Conjured Item", 10, 20))
        expected_sell_in = 9
        expected_quality = 18
        # act
        item.update()
        # assert
        self.assertEqual(expected_sell_in, item.item.sell_in)
        self.assertEqual(expected_quality, item.item.quality)

    def test_item_quality_does_not_go_below_min_quantity(self):
        # arrange the test
        item = Conjured(Item("Conjured Item", 10, 0))
        expected_sell_in = 9
        expected_quality = 0
        # act
        item.update()
        # assert
        self.assertEqual(expected_sell_in, item.item.sell_in)
        self.assertEqual(expected_quality, item.item.quality)

    def test_item_quality_decreases_twice_as_fast_after_sell_in(self):
        # arrange the test
        item = Conjured(Item("Conjured Item", 0, 20))
        expected_sell_in = -1
        expected_quality = 16
        # act
        item.update()
        # assert
        self.assertEqual(expected_sell_in, item.item.sell_in)
        self.assertEqual(expected_quality, item.item.quality)

    def test_item_quality_does_not_go_below_min_quality(self):
         # arrange the test
        item = Conjured(Item("Conjured Item", 0, 1))
        expected_sell_in = -1
        expected_quality = 0
        # act
        item.update()
        # assert
        self.assertEqual(expected_sell_in, item.item.sell_in)
        self.assertEqual(expected_quality, item.item.quality)

if __name__ == '__main__':
    unittest.main()

