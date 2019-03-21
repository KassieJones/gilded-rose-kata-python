# -*- coding: utf-8 -*-

class Default(object):

    def __init__(self, item):
        self.item = item

    def lower_quality(self):
        if self.item.quality > 0:
            self.item.quality = self.item.quality - 1

    def lower_sell_in(self):
        self.item.sell_in = self.item.sell_in - 1

    def add_quality(self):
        if self.item.quality < 50:
            self.item.quality = self.item.quality + 1

    def update_quality(self):
        self.lower_quality()
        self.lower_sell_in()

        if self.item.sell_in < 0:
            self.lower_quality()


class AgedBrie(Default):

    def update_quality(self):
        self.add_quality()
        self.lower_sell_in()
        if self.item.sell_in < 0:
            self.add_quality()


class Backstage(Default):
    def quality_zeroed(self):
        self.item.quality = 0

    def update_quality(self):
        self.add_quality()
        if self.item.sell_in <= 10:
            self.add_quality()
        if self.item.sell_in <= 5:
            self.add_quality()
        self.lower_sell_in()
        if self.item.sell_in < 0:
            self.quality_zeroed()


class Sulfuras(Default):

    def update_quality(self):
        pass


class Conjured(Default):
    def decrease_quality(self):
        Default.decrease_quality(self)
        Default.decrease_quality(self)

class GildedRose(object):
    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if item.name == "Aged Brie":
                updater = AgedBrie(item)
                updater.update_quality()
            elif item.name == "Backstage passes to a TAFKAL80ETC concert":
                updater = Backstage(item)
                updater.update_quality()
            elif item.name == "Sulfuras, Hand of Ragnaros":
                updater = Sulfuras(item)
                updater.update_quality()
            elif item.name == "Conjured Mana Cake":
                updater = Sulfuras(item)
                updater.update_quality()
            else:
                updater = Default(item)
                updater.update_quality()



class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)