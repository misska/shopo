#!/usr/bin/env python
# coding=utf-8

from Importer import Importer

class SlovanskyDumImporter(Importer):
    name = 'Slovanský dům'
    url = 'http://www.slovanskydum.cz/obchody'

    def parse(self):
        for shopList in self.soup.findAll("div", {"class":"shops"}):
            for name in shopList.findAll("cufontext"):
                if isinstance(name.text, basestring):
                    self.shops.append(name.text)