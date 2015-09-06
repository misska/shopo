#!/usr/bin/env python
# coding=utf-8

from Importer import Importer

class SestkaImporter(Importer):
    name = 'OC Šestka'
    url = 'https://www.oc-sestka.cz/obchody/'

    def parse(self):
        for shopList in self.soup.findAll("div", {"class":"seznam-placeholder"}):
            for link in shopList.findAll("a"):
                if isinstance(link.text, basestring):
                    self.shops.append(link.text)
