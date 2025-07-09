# -*- coding: utf-8 -*-
from python.constants import SULFURAS_QUALITY, MAX_ITEM_QUALITY


class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if item.name != "Aged Brie" and item.name != "Backstage passes to a TAFKAL80ETC concert":
                if item.quality > 0:
                    if item.name != "Sulfuras, Hand of Ragnaros":
                        item.quality = item.quality - 1
            else:
                if item.quality < 50:
                    item.quality = item.quality + 1
                    if item.name == "Backstage passes to a TAFKAL80ETC concert":
                        if item.sell_in < 11:
                            if item.quality < 50:
                                item.quality = item.quality + 1
                        if item.sell_in < 6:
                            if item.quality < 50:
                                item.quality = item.quality + 1
            if item.name != "Sulfuras, Hand of Ragnaros":
                item.sell_in = item.sell_in - 1
            if item.sell_in < 0:
                if item.name != "Aged Brie":
                    if item.name != "Backstage passes to a TAFKAL80ETC concert":
                        if item.quality > 0:
                            if item.name != "Sulfuras, Hand of Ragnaros":
                                item.quality = item.quality - 1
                    else:
                        item.quality = item.quality - item.quality
                else:
                    if item.quality < 50:
                        item.quality = item.quality + 1


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

# As per requirements, Item class cannot be modified so we can implement a strategy to allow items to manage their own
# quality. This has the added benefit of supporting future items without needing to modify the GildedRose class,
# adhering to the Open Close principle to allow for
class UpdatableItem:
    def __init__(self, item: Item):
        self.item = item

    def update(self):
        raise NotImplementedError

class Sulfuras(UpdatableItem):
    def update(self):
        # Sulfuras attributes do not change
        # throw AssertionError when quality is not 80
        assert self.item.quality == SULFURAS_QUALITY, f"Sulfuras quality should always be {SULFURAS_QUALITY}"

class AgedBrie(UpdatableItem):
    def update(self):
        self.item.sell_in -= 1
        self.item.quality += 1
        # GildedRoseRequirements.md states that Aged Brie increases in quality the older it gets,
        # However, looking at the test approvals it seems that once the sell_in has passed, it increases by 2
        if self.item.sell_in < 0:
            self.item.quality += 1
        self.item.quality = max(MAX_ITEM_QUALITY, self.item.quality)