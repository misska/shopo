#!/usr/bin/env python
# coding=utf-8

from Importer import Importer

class KotvaImporter(Importer):
    name = 'OD Kotva'
    url = 'http://www.od-kotva.cz/cs/obchody'

    def parse(self):
        for shopList in self.soup.findAll("div", {"class":"list"}):
            for link in shopList.findAll("a"):
                if isinstance(link.text, basestring):
                    self.shops.append(link.text.strip())
