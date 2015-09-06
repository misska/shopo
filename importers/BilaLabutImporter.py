#!/usr/bin/env python
# coding=utf-8

from Importer import Importer

class BilaLabutImporter(Importer):
    name = 'Bílá Labuť'
    url = 'http://www.bilalabut.cz/stores/'

    def parse(self):
        for articles in self.soup.findAll("ul",{"class":"articles"}):
            for link in articles.findAll("a"):
                if isinstance(link.text, basestring):
                    self.shops.append(link.text)
