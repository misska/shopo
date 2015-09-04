#!/usr/bin/env python
# coding=utf-8

import json
import webapp2

import model

def shoppingCentreToDict(shoppingCentre):
    return {
        'name': shoppingCentre.name,
        'address': shoppingCentre.address,
        'coords': shoppingCentre.coords,
        'shops': [shop.get().name for shop in shoppingCentre.shops]
    }

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world')

class ShoppingCentresHandler(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'application/json'
        shoppingCentres = [shoppingCentreToDict(row) for row in model.ShoppingCentre.query()]
        self.response.write(json.dumps(shoppingCentres, ensure_ascii=False))

app = webapp2.WSGIApplication([
    ('/api/', MainHandler),
    ('/api/shopping-centres', ShoppingCentresHandler)
], debug=True)
