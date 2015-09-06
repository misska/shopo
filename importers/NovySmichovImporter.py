#!/usr/bin/env python
# coding=utf-8

from Importer import Importer

class NovySmichovImporter(Importer):
    name = 'OC Nový Smíchov'
    url = 'http://cz.club-onlyou.com/Novy-Smichov/Nakupovani'

    def parse(self):
        for shopList in self.soup.findAll("section", {"class":"shopListing"}):
            for link in shopList.findAll("a"):
                if isinstance(link.text, basestring):
                    self.shops.append(link.text)
