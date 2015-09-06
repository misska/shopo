#!/usr/bin/env python
# coding=utf-8

from Importer import Importer

class NovodvorskaPlazaImporter(Importer):
    name = 'Novodvorská Plaza'
    url = 'http://cz.club-onlyou.com/Novodvorska-Plaza/Nakupovani'

    def parse(self):
        for shopList in self.soup.findAll("section", {"class":"shopListing"}):
            for link in shopList.findAll("a"):
                if isinstance(link.text, basestring):
                    self.shops.append(link.text)
