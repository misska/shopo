#!/usr/bin/env python
# coding=utf-8

import urllib2
from bs4 import BeautifulSoup

from Importer import Importer

class FlorentinumImporter(Importer):
    name = 'Florentinum'
    links = [
        'http://www.florentinum.cz/cs/obchody/obchodni-pasaz/', 
        'http://www.florentinum.cz/cs/obchody/piazza-a-ulice-na-florenci/'
    ]
    soups = []

    def download(self):
        for link in self.links:
            sock = urllib2.urlopen(link)
            html = sock.read()
            self.soups.append(BeautifulSoup(html))

    def parse(self):
        for soup in self.soups:
            shopMap = soup.find("map",{"id":"Map"})
            for area in shopMap.findAll("area", {"shape":"poly"}):
                rel = area.get('rel')
                name = ' '.join(rel)
                if isinstance(name, basestring):
                    self.shops.append(name)