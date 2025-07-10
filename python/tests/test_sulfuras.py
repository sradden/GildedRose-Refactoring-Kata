import unittest
from python.gilded_rose import Sulfuras, Item

class SulfurasTest(unittest.TestCase):
    def test_item_does_not_change(self):
        item = Sulfuras(Item("Sulfuras, Hand of Ragnaros", 0, 80))
        initial_quality = item.item.quality
        initial_sell_in = item.item.sell_in
        item.update()
        self.assertEqual(initial_quality, item.item.quality)
        self.assertEqual(initial_sell_in, item.item.sell_in)

    def test_assert_error_thrown_if_quality_not_eighty(self):
        item = Sulfuras(Item("Sulfuras, Hand of Ragnaros", 0, 79))
        with self.assertRaises(AssertionError):
            item.update()

    if __name__ == '__main__':
        unittest.main()