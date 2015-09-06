#!/usr/bin/env python
# coding=utf-8

from Importer import Importer

class GalerieButoviceImporter(Importer):
    name = 'Galerie Butovice'
    url = 'http://www.galerie-butovice.cz/obchody-a-sluzby/#filter-all'

    def parse(self):
        for shop in self.soup.findAll("li",{"class":"oc-brand-preview"}):
            link = shop.find("a", recursive=False)
            if isinstance(link.text, basestring):
                self.shops.append(link.text)
