# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose

class GildedRoseTest(unittest.TestCase):
    def test_AB_under11_under50(self):
        items = [Item("Aged Brie", 5, 49)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(4, items[0].sell_in)
        self.assertEqual(50, items[0].quality)

    def test_AB_under11_over50(self):
        items = [Item("Aged Brie", 5, 51)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(4, items[0].sell_in)
        self.assertEqual(51, items[0].quality)

    def test_AB_over11_under50(self):
        items = [Item("Aged Brie", 12, 49)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(11, items[0].sell_in)
        self.assertEqual(50, items[0].quality)

    def test_AB_over11_over50(self):
        items = [Item("Aged Brie", 12, 51)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(11, items[0].sell_in)
        self.assertEqual(51, items[0].quality)

    def test_AB_under0_under50(self):
        items = [Item("Aged Brie", -1, 49)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].sell_in)
        self.assertEqual(50, items[0].quality)

    def test_AB_under0_over50(self):
        items = [Item("Aged Brie", -1, 51)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].sell_in)
        self.assertEqual(51, items[0].quality)

    def test_BP_under11_under50(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 5, 49)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(4, items[0].sell_in)
        self.assertEqual(50, items[0].quality)

    def test_BP_under11_over50(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 5, 51)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(4, items[0].sell_in)
        self.assertEqual(51, items[0].quality)

    def test_BP_over11_under50(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 12, 49)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(11, items[0].sell_in)
        self.assertEqual(50, items[0].quality)

    def test_BP_over11_over50(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 12, 51)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(11, items[0].sell_in)
        self.assertEqual(51, items[0].quality)

    def test_BP_under0_over50(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", -1, 51)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].sell_in)
        self.assertEqual(0, items[0].quality)

    def test_BP_under0_under50(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", -1, 49)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].sell_in)
        self.assertEqual(0, items[0].quality)

    def test_SUL_under11_under50(self):
        items = [Item("Sulfuras", 5, 49)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(4, items[0].sell_in)
        self.assertEqual(48, items[0].quality)

    def test_SUL_under11_over50(self):
        items = [Item("Sulfuras", 5, 51)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(4, items[0].sell_in)
        self.assertEqual(50, items[0].quality)

    def test_SUL_over11_under50(self):
        items = [Item("Sulfuras", 12, 49)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(11, items[0].sell_in)
        self.assertEqual(48, items[0].quality)

    def test_SUL_over11_over50(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 12, 51)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(12, items[0].sell_in)
        self.assertEqual(51, items[0].quality)

    def test_SUL_under0_over50(self):
        items = [Item("Sulfuras, Hand of Ragnaros", -1, 51)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].sell_in)
        self.assertEqual(51, items[0].quality)

    def test_SUL_under0_under50(self):
        items = [Item("Sulfuras, Hand of Ragnaros", -1, 49)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].sell_in)
        self.assertEqual(49, items[0].quality)


    def test_ANY_under11_under50(self):
        items = [Item("ANY", 5, 49)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(4, items[0].sell_in)
        self.assertEqual(48, items[0].quality)

    def test_ANY_under11_over50(self):
        items = [Item("ANY", 5, 51)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(4, items[0].sell_in)
        self.assertEqual(50, items[0].quality)

    def test_ANY_over11_under50(self):
        items = [Item("ANY", 12, 49)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(11, items[0].sell_in)
        self.assertEqual(48, items[0].quality)

    def test_ANY_over11_over50(self):
        items = [Item("ANY", 12, 51)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(11, items[0].sell_in)
        self.assertEqual(50, items[0].quality)

    def test_ANY_under0_over50(self):
        items = [Item("ANY", -1, 51)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].sell_in)
        self.assertEqual(49, items[0].quality)

    def test_ANY_under0_under50(self):
        items = [Item("ANY", -1, 49)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].sell_in)
        self.assertEqual(47, items[0].quality)


    def test_CON_under11_under50(self):
        items = [Item("Conjured Mana Cake", 5, 49)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(4, items[0].sell_in)
        self.assertEqual(47, items[0].quality)


if __name__ == '__main__':
    unittest.main()
