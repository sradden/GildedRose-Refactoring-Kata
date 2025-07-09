import unittest

from python.constants import MAX_QUALITY
from python.gilded_rose import AgedBrie, Item

class AgedBrieTest(unittest.TestCase):
    def test_item_is_updated(self):
        item = AgedBrie(Item("Aged Brie", 2, 0))
        expected_quality = item.item.quality +1
        expected_sell_in = item.item.sell_in - 1
        item.update()
        self.assertEqual(expected_quality, item.item.quality)
        self.assertEqual(expected_sell_in, item.item.sell_in)

    def test_quality_does_not_exceed_max_quality(self):
        item = AgedBrie(Item("Aged Brie", 2, 50))
        expected_quality = MAX_QUALITY
        item.update()
        self.assertEqual(expected_quality, item.item.quality)

    def test_quality_increases_twice_as_fast_after_sell_in(self):
        item = AgedBrie(Item("Aged Brie", 0, 10))
        expected_quality = item.item.quality + 2
        expected_sell_in = item.item.sell_in - 1
        item.update()
        self.assertEqual(expected_quality, item.item.quality)
        self.assertEqual(expected_sell_in, item.item.sell_in)

if __name__ == '__main__':
    unittest.main()
