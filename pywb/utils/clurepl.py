# -*- encoding: utf-8 -*-
#
# CLU repl script (q.v. Makefile and Python-CLU)
#

import importlib
import pywb
from clu.fs.filesystem import wd, Directory

# basedir = wd().parent().parent()
# basedir = Directory(__file__).parent().parent()
basedir = wd()
importables = basedir.importables('pywb')

for dotpath in importables:
    try:
        importlib.import_module(dotpath)
        print(f"Imported {dotpath}")
    except ImportError:
        print(f"FAILED TO IMPORT: {dotpath}")

