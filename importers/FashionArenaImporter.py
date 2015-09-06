#!/usr/bin/env python
# coding=utf-8

from Importer import Importer

class FashionArenaImporter(Importer):
    name = 'Fashion Arena Outlet Center'
    url = 'http://www.fashion-arena.cz/cs/znacky'

    def parse(self):
        for shopList in self.soup.findAll("ul",{"class":"list-unstyled"}):
            for link in shopList.findAll("a"):
                if isinstance(link.text, basestring):
                    self.shops.append(link.text)
