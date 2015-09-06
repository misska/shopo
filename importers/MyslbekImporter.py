#!/usr/bin/env python
# coding=utf-8

from Importer import Importer

class MyslbekImporter(Importer):
    name = 'Nákupní galerie Myslbek'
    url = 'http://www.ngmyslbek.cz/CZ/guess-jeans'

    def parse(self):
        for shopList in self.soup.findAll("div", {"class":"obchody"}):
            for link in shopList.findAll("a"):
                if isinstance(link.text, basestring):
                    self.shops.append(link.text)
