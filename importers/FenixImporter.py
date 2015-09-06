#!/usr/bin/env python
# coding=utf-8

from Importer import Importer

class FenixImporter(Importer):
    name = 'NC Fénix'
    url = 'http://www.ncfenix.cz/cs/obchody'

    def parse(self):
        for shopList in self.soup.findAll("ul",{"class":"sitemap-list"}):
            for link in shopList.findAll("a"):
                if isinstance(link.text, basestring):
                    self.shops.append(link.text)
