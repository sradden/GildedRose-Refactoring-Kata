# -*- coding: utf-8 -*-
from python.constants import SULFURAS_QUALITY, MAX_QUALITY, MIN_QUALITY

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

    def __repr__(self):
        return self.item.__repr__()

class Sulfuras(UpdatableItem):
    # Sulfuras attributes do not change
    def update(self):
        # throw AssertionError when quality is not 80
        assert self.item.quality == SULFURAS_QUALITY, f"Sulfuras quality should always be {SULFURAS_QUALITY}"

class AgedBrie(UpdatableItem):
    # Quality increases as the item ages.
    # Increases by 1 until sell_in expires, then increases by 2.
    # Maximum quality is 50.
    def update(self):
        self.item.sell_in -= 1
        self.item.quality += 1
        # GildedRoseRequirements.md states that Aged Brie increases in quality the older it gets,
        # However, looking at the test approvals it seems that once the sell_in has passed, it increases by 2
        if self.item.sell_in < 0:
            self.item.quality += 1
        self.item.quality = min(MAX_QUALITY, self.item.quality)

class Standard(UpdatableItem):
    # Quality decreases as the item ages.
    # Decreases by 1 until sell_in expires, then decreases by 2.
    # Minimum quality is 0.
    def update(self):
        self.item.sell_in -= 1
        self.item.quality -= 1
        # If the sell_in has passed, the quality decreases by 2
        if self.item.sell_in < 0:
            self.item.quality -= 1
        # quality cannot be negative
        self.item.quality = max(MIN_QUALITY, self.item.quality)

class BackstagePass(UpdatableItem):
    # increases in quality as the concert date approaches but drops to 0 after the concert.
    # The closer the concert date, the more it increases in quality.
    # Maximum quality is 50.
    def update(self):
        self.item.sell_in -= 1
        if self.item.sell_in < 0:
            self.item.quality = 0
        elif self.item.sell_in < 5:
            self.item.quality += 3
        elif self.item.sell_in < 10:
            self.item.quality += 2
        else:
            self.item.quality += 1
        # quality does not exceed MAX_QUALITY
        self.item.quality = min(MAX_QUALITY, self.item.quality)

class Conjured(UpdatableItem):
    # Degrades in quality twice as fast as normal items.
    # Quality decreases by 2 until sell_in expires, then decreases by 4.
    # Minimum quality is 0.
    def update(self):
        self.item.sell_in -= 1
        self.item.quality -= 2
        # If the sell_in has passed, the quality decreases by 2 more
        if self.item.sell_in < 0:
            self.item.quality -= 2
        # quality cannot be negative
        self.item.quality = max(MIN_QUALITY, self.item.quality)

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        updatable_items = [self.create_updatable_item(item) for item in self.items]
        for updatable_item in updatable_items:
            updatable_item.update()

    @staticmethod
    def create_updatable_item(item: Item) -> UpdatableItem:
        # TODO: Refactor this method if item names cannot be used to determine the type of item.
        if item.name.lower() == "sulfuras, hand of ragnaros":
            return Sulfuras(item)
        elif item.name.lower() == "aged brie":
            return AgedBrie(item)
        elif item.name.lower() == "backstage passes to a tafkal80etc concert":
            return BackstagePass(item)
        elif item.name.lower().startswith("conjured"):
            return Conjured(item)
        else:
            return Standard(item)