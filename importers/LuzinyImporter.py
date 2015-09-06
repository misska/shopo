#!/usr/bin/env python
# coding=utf-8

from Importer import Importer

class LuzinyImporter(Importer):
    name = 'OC Lužiny'
    url = 'http://www.ocluziny.cz/new/cs/obchody'

    def parse(self):
        for category in self.soup.findAll("div", {"class":"kategorie"}):
            for link in category.findAll("a"):
                if isinstance(link.text, basestring):
                    self.shops.append(link.text)
