#!/usr/bin/env python
# coding=utf-8

import urllib
import urllib2
from bs4 import BeautifulSoup

from Importer import Importer

class AtriumImporter(Importer):
    name = 'Atrium Flóra'
    url = 'http://www.atrium-flora.cz/wp-admin/admin-ajax.php'

    def download(self):
        data = urllib.urlencode({
            'type' : 'aere_stores', 
            'p' : 1000, 
            'action' : 'loadpage', 
            't' : 'store', 
            'next' : 1
        })
        req = urllib2.Request(self.url, data)
        sock = urllib2.urlopen(req)
        html = sock.read()
        self.soup = BeautifulSoup(html, "html5lib")

    def parse(self):
        for image in self.soup.findAll("img"):
            name = image.get('alt')
            if isinstance(name, basestring):
                self.shops.append(name)
