#!/usr/bin/env python
# coding=utf-8

from Importer import Importer

class GalerieHarfaImporter(Importer):
    name = 'Galerie Harfa'
    url = 'http://www.galerieharfa.cz/cs/obchody/vse/'

    def parse(self):
        for shopList in self.soup.findAll("ul",{"class":"post-list"}):
            for link in shopList.findAll("a"):
                if isinstance(link.text, basestring):
                    self.shops.append(link.text)
