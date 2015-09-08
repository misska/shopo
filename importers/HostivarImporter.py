#!/usr/bin/env python
# coding=utf-8

from Importer import Importer

class HostivarImporter(Importer):
    name = 'Park Hostivař'
    url = 'http://www.parkhostivar.cz/obchody-a-sluzby'

    def parse(self):
        for col in self.soup.findAll("div", {"class": "obchody-col"}):
            for link in col.findAll("a"):
                if isinstance(link.text, basestring):
                    self.shops.append(link.text)
