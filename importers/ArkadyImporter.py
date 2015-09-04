#!/usr/bin/env python
# coding=utf-8

from Importer import Importer

class ArkadyImporter(Importer):
    name = 'Arkády Pankrác'
    url = 'http://www.arkady-pankrac.cz/cz/obchody'

    def parse(self):
        for shopList in self.soup.findAll("div",{"class":"shop-list"}):
            for link in shopList.findAll("a"):
                if isinstance(link.text, basestring):
                    self.shops.append(link.text)
