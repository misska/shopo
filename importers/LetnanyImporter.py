#!/usr/bin/env python
# coding=utf-8

from Importer import Importer

class LetnanyImporter(Importer):
    name = 'OC Letňany'
    url = 'http://www.oc-letnany.cz/obchody-a-sluzby/'

    def parse(self):
        for shopList in self.soup.findAll("div", {"class":"oc-brands-preview-list"}):
            for name in shopList.findAll("div", {"class":"oc-brands-preview-name"}):
                if isinstance(name.text, basestring):
                    self.shops.append(name.text)