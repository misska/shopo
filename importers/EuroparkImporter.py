#!/usr/bin/env python
# coding=utf-8

from Importer import Importer

class EuroparkImporter(Importer):
    name = 'Europark Štěrboholy'
    url = 'http://www.europark.cz/cz/obchody_a_sluzby'

    def parse(self):
        for shopList in self.soup.findAll("div",{"class":"shop-list"}):
            for name in shopList.findAll("td", {"class":"last"}):
                for link in name.findAll("a"):
                    if isinstance(link.text, basestring):
                        self.shops.append(link.text)
