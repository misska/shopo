#!/usr/bin/env python
# coding=utf-8

from Importer import Importer

class QuadrioImporter(Importer):
    name = 'Quadrio'
    url = 'http://www.quadrio.cz/obchody/kategorie'

    def parse(self):
        for shopList in self.soup.findAll("div", {"class":"shopsWrapper"}):
            for name in shopList.findAll("div", {"class":"text"}):
                for link in name.findAll("a"):
                    if isinstance(link.text, basestring):
                        self.shops.append(link.text)