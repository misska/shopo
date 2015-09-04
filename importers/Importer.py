#!/usr/bin/env python
# coding=utf-8

import urllib2
from bs4 import BeautifulSoup

import model

class Importer(object):
    soup = ''
    shops = []

    def download(self):
        sock = urllib2.urlopen(self.url)
        html = sock.read()
        self.soup = BeautifulSoup(html)

    def save(self):
        shoppingCentre = model.ShoppingCentre.query(model.ShoppingCentre.name == self.name.decode('utf-8')).fetch(1)[0]
        for shopName in self.shops:
            shop = model.Shop.get_or_insert(shopName, name=shopName)
            if not shop.key in shoppingCentre.shops:
                shoppingCentre.shops.append(shop.key)
                shoppingCentre.put()
        return shoppingCentre

    def run(self):
        self.download()
        self.parse()
        return self.save()
