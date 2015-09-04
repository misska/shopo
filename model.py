from google.appengine.ext import ndb

class Shop(ndb.Model):
    name = ndb.StringProperty()

class ShoppingCentre(ndb.Model):
    name = ndb.StringProperty()
    address = ndb.StringProperty(indexed=False)
    coords = ndb.StringProperty()
    shops = ndb.KeyProperty(kind=Shop, repeated=True)

