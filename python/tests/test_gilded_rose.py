# -*- coding: utf-8 -*-
import unittest
from python.gilded_rose import Item, GildedRose, Sulfuras, AgedBrie, BackstagePass, Conjured, Standard


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("foo", items[0].name)

    def test_create_updatable_item_returns_sulfuras(self):
        # arrange
        item = Item("Sulfuras, Hand of Ragnaros", 10, 80)
        # act
        updatable = GildedRose.create_updatable_item(item)
        # assert
        assert isinstance(updatable, Sulfuras)

    def test_create_updatable_item_returns_aged_brie(self):
        # arrange
        item = Item("Aged Brie", 10, 50)
        # act
        updatable = GildedRose.create_updatable_item(item)
        # assert
        assert isinstance(updatable, AgedBrie)

    def test_create_updatable_item_returns_backstage_pass(self):
        # arrange
        item = Item("Backstage Passes to a TAFKAL80ETC Concert", 10, 50)
        # act
        updatable = GildedRose.create_updatable_item(item)
        # assert
        assert isinstance(updatable, BackstagePass)

    def test_create_updatable_item_returns_conjured(self):
        # arrange
        item = Item("Conjured Item", 10, 50)
        # act
        updatable = GildedRose.create_updatable_item(item)
        # assert
        assert isinstance(updatable, Conjured)

    def test_create_updatable_item_returns_standard(self):
        # arrange
        item = Item("Foo", 10, 50)
        # act
        updatable = GildedRose.create_updatable_item(item)
        # assert
        assert isinstance(updatable, Standard)

if __name__ == '__main__':
    unittest.main()
