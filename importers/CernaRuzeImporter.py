#!/usr/bin/env python
# coding=utf-8

from Importer import Importer

class CernaRuzeImporter(Importer):
    name = 'Nákupní pasáž Černá růže'
    url = 'http://www.cernaruze.cz/obchody/'

    def parse(self):
        for shopList in self.soup.findAll("ul", {"class":"postList"}):
            for name in shopList.findAll("div", {"class":"postListText"}):
                for link in name.findAll("a"):
                    if isinstance(link.text, basestring):
                        self.shops.append(link.text)