#!/usr/bin/env python
# coding=utf-8

from Importer import Importer

class AvionImporter(Importer):
    name = 'Avion Shopping Park'
    url = 'https://www.prague.avion.cz/cs-cz/store-locator'

    def parse(self):
        for storesList in self.soup.findAll("div",{"id":"allStoresList"}):
            for link in storesList.findAll("a"):
                if isinstance(link.text, basestring):
                    self.shops.append(link.text)
