#!/usr/bin/env python
# coding=utf-8

from Importer import Importer

class KrakovImporter(Importer):
    name = 'Centrum Krakov'
    url = 'http://www.centrumkrakov.cz/cs/mapa-obchody.php'

    def parse(self):
        for shopList in self.soup.findAll("div",{"class":"obchod-seznam"}):
            for link in shopList.findAll("a"):
                if isinstance(link.text, basestring):
                    self.shops.append(link.text)
