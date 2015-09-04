#!/usr/bin/env python
# coding=utf-8

import csv
import webapp2
import sys
import os.path

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'lib'))

from google.appengine.ext import blobstore
from google.appengine.ext.webapp import blobstore_handlers

import model
import importers
from importers import *


def getImporter(importerName):
    importerModule = globals()[importerName]
    importerClass = getattr(importerModule, importerName)
    importer = importerClass()
    return importer

class ImportShoppingCentresHandler(webapp2.RequestHandler):
    def get(self):
        upload_url = blobstore.create_upload_url('/import/upload-shopping-centres')
 
        html_string = """
        <form action="%s" method="POST" enctype="multipart/form-data">
        Upload File:
        <input type="file" name="file"> <br>
        <input type="submit" name="submit" value="Submit">
        </form>""" % upload_url
 
        self.response.write(html_string)

class UploadShoppingCentresHandler(blobstore_handlers.BlobstoreUploadHandler):
    def post(self):
        upload_files = self.get_uploads('file')  # 'file' is file upload field in the form
        blob_info = upload_files[0]
        
        blob_reader = blobstore.BlobReader(blob_info.key())
        reader = csv.reader(blob_reader, delimiter=';')
        for row in reader:
            name, address, coords = row
            entry = model.ShoppingCentre(name=name, address=address, coords=coords)
            entry.put()
 
        blobstore.delete(blob_info.key())  # optional: delete file after import
        self.redirect('/api/shopping-centres')

class ImportAllShopsHandler(webapp2.RequestHandler):
    def get(self):
        results = []
        for importerName in importers.__dict__['__all__']:
            if not importerName == 'Importer':
                importer = getImporter(importerName)
                results.append(importer.run())

        self.response.write(results)

class ImportShopHandler(webapp2.RequestHandler):
    def get(self, shoppingCentre):
        importerName = shoppingCentre + 'Importer'
        importer = getImporter(importerName)
        self.response.write(importer.run())

app = webapp2.WSGIApplication([
    ('/import/shopping-centres', ImportShoppingCentresHandler),
    ('/import/upload-shopping-centres', UploadShoppingCentresHandler),
    ('/import/shops/all', ImportAllShopsHandler),
    ('/import/shops/(.*)', ImportShopHandler),
], debug=True)
