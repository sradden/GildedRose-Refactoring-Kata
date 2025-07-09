import unittest

from python.constants import MAX_QUALITY
from python.gilded_rose import BackstagePass, Item

class BackstagePassTest(unittest.TestCase):
    def test_item_is_updated(self):
        # arrange
        item = BackstagePass(Item("Backstage passes to a TAFKAL80ETC concert", 15, 20))
        expected_quality = item.item.quality + 1
        expected_sell_in = item.item.sell_in - 1
        # act
        item.update()
        # assert
        self.assertEqual(expected_quality, item.item.quality)
        self.assertEqual(expected_sell_in, item.item.sell_in)

    def test_quality_does_not_exceed_max_quality(self):
        # arrange
        item = BackstagePass(Item("Backstage passes to a TAFKAL80ETC concert", 10, 50))
        expected_quality = MAX_QUALITY
        # act
        item.update()
        # assert
        self.assertEqual(expected_quality, item.item.quality)

    def test_quality_increases_by_two_when_sell_in_is_ten_or_less(self):
        # arrange
        item = BackstagePass(Item("Backstage passes to a TAFKAL80ETC concert", 10, 20))
        expected_quality = item.item.quality + 2
        expected_sell_in = item.item.sell_in - 1
        # act
        item.update()
        # assert
        self.assertEqual(expected_quality, item.item.quality)
        self.assertEqual(expected_sell_in, item.item.sell_in)

    def test_quality_increases_by_three_when_sell_in_is_five_or_less(self):
        # arrange
        item = BackstagePass(Item("Backstage passes to a TAFKAL80ETC concert", 5, 20))
        expected_quality = item.item.quality + 3
        expected_sell_in = item.item.sell_in - 1
        # act
        item.update()
        # assert
        self.assertEqual(expected_quality, item.item.quality)
        self.assertEqual(expected_sell_in, item.item.sell_in)

    def test_quality_drops_to_zero_after_concert(self):
        # arrange
        item = BackstagePass(Item("Backstage passes to a TAFKAL80ETC concert", 0, 20))
        expected_quality = 0
        expected_sell_in = item.item.sell_in - 1
        # act
        item.update()
        # assert
        self.assertEqual(expected_quality, item.item.quality)
        self.assertEqual(expected_sell_in, item.item.sell_in)

if __name__ == '__main__':
    unittest.main()
