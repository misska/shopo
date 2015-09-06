#!/usr/bin/env python
# coding=utf-8

from Importer import Importer

class GalerieAtriumImporter(Importer):
    name = 'Nákupní galerie Atrium'
    url = 'http://www.nakupnigalerieatrium.cz/index.php/obchody-a-sluzbycz'

    def parse(self):
        menu = self.soup.find("ul", {"class":"menu-sidebar"})
        for shopList in menu.findAll("ul"):
            for link in shopList.findAll("a"):
                if isinstance(link.text, basestring):
                    self.shops.append(link.text)
