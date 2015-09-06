#!/usr/bin/env python
# coding=utf-8

from Importer import Importer

class DBKImporter(Importer):
    name = 'DBK Budějovická'
    url = 'http://www.dbkpraha.cz/najemci.php'

    def parse(self):
        for shopList in self.soup.findAll("div",{"class":"rentAlphabetList"}):
            for name in shopList.findAll("div", {"class":"rentAlphabetLink"}):
                for link in name.findAll("a"):
                    if isinstance(link.text, basestring):
                        self.shops.append(link.text)