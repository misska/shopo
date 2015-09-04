import os
import glob

modules = glob.glob(os.path.dirname(__file__) + "/*Importer.py")
__all__ = [os.path.basename(f)[:-3] for f in modules]