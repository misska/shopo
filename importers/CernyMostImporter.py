#!/usr/bin/env python
# coding=utf-8

from Importer import Importer

class CernyMostImporter(Importer):
    name = 'Centrum Černý Most'
    url = 'http://www.centrumcernymost.cz/W/do/centre/vse-obchody'

    def parse(self):
        boutiques = self.soup.find("div", {"id":"pcp_main_boutiques_content"})
        for name in boutiques.findAll("div", {"class":"boutiques_bottom"}):
            if isinstance(name.text, basestring):
                    self.shops.append(name.text)