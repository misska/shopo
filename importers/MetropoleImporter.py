#!/usr/bin/env python
# coding=utf-8

from Importer import Importer

class MetropoleImporter(Importer):
    name = 'Metropole Zličín'
    url = 'http://www.metropole.cz/obchody.html'

    def parse(self):
        for shopList in self.soup.findAll("ul",{"class":"mt5"}):
            for link in shopList.findAll("a"):
                if isinstance(link.text, basestring):
                    self.shops.append(link.text)
