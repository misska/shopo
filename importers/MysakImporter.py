#!/usr/bin/env python
# coding=utf-8

from Importer import Importer

class MysakImporter(Importer):
    name = 'Myšák Gallery'
    url = 'http://www.gallerymysak.cz/moda-a-sluzby'

    def parse(self):
        for shopList in self.soup.findAll("div", {"id":"right"}):
            for link in shopList.findAll("a"):
                if isinstance(link.text, basestring):
                    self.shops.append(link.text)
