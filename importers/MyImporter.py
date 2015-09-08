#!/usr/bin/env python
# coding=utf-8

from Importer import Importer

class MyImporter(Importer):
    name = 'My Národní'
    url = 'http://www.mystores.cz/department-1396.html'

    def parse(self):
        for department in self.soup.findAll("section", {"class":"departments"}):
            for shopList in department.findAll("ul"):
                for link in shopList.findAll("a"):
                    if isinstance(link.text, basestring):
                        self.shops.append(link.text)
