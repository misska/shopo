#!/usr/bin/env python
# coding=utf-8

import urllib2
from bs4 import BeautifulSoup

from Importer import Importer

class BBCImporter(Importer):
    name = 'BB Centrum Nová Brumlovka'
    url = 'http://www.bbcentrum.cz/cs/bb-centrum/obchody-a-sluzby/'
    soups = []

    def download(self):
        super(BBCImporter, self).download()
        links = self.parseLinks()

        for link in links:
            sock = urllib2.urlopen(link)
            html = sock.read()
            self.soups.append(BeautifulSoup(html, "html5lib"))

    def parseLinks(self):
        links = []
        categories = self.soup.find("ul", {"class":"Categories"})
        for link in categories.findAll("a"):
            href = link.get('href')
            if isinstance(href, basestring):
                links.append(href)
        return links

    def parse(self):
        for soup in self.soups:
            services = soup.find("ol",{"class":"Services"})
            for name in services.findAll("span", {"class":"t"}):
                if isinstance(name.text, basestring):
                    self.shops.append(name.text)