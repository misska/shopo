#!/usr/bin/env python
# coding=utf-8

from Importer import Importer

class PalladiumImporter(Importer):
    name = 'Palladium'
    url = 'http://www.palladiumpraha.cz/plan-centra/'

    def parse(self):
        for category in self.soup.findAll("div", {"class":"list-segments__category"}):
            for shopList in category.findAll("ul"):
                for link in shopList.findAll("a"):
                    if isinstance(link.text, basestring):
                        self.shops.append(link.text.strip())
