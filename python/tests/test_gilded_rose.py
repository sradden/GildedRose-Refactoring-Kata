# -*- coding: utf-8 -*-
import unittest
from python.gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("foo", items[0].name)

    def test_non_sulfuras_item_quality_cannot_exceed_fifty(self):
        items = [Item("foo", 2, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(50, items[0].quality)



if __name__ == '__main__':
    unittest.main()
