#!/usr/bin/env python
import pip

# list of packages required to build lurvescrappy script
bs4="bs4"
feedparser="feedparser"

print('Checking Beautiful Soup 4 dependancies...')
try:
    __import__(bs4)
except ImportError:
    print('Installing Bueatiful Soup 4 (BS4) via Pip')
    pip.main(['install', bs4])

print('Checking feedparser dependancies...')
try:
    __import__(feedparser)
except ImportError:
    print('Installing feedparser via Pip')
    pip.main(['install', feedparser])

print('All done')
