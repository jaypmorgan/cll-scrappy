#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime
from lxml import etree, html
import dateutil.relativedelta
import sys, argparse
import urllib2
from xml.etree import ElementTree as etree
import lxml.etree

# program description
parser = argparse.ArgumentParser(description="""Script for procedurally
getting the command line love arguments from the ubuntu podcast website.
The output of this script can be defined using optional flags
""")

# program flags
parser.add_argument('--all', dest='getall', help='get all the command line loves from the archives')
args = parser.parse_args()

#CLLs
clls = []

def get_source():
	hdr= {
		'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       	'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       	'Accept-Encoding': 'none',
       	'Accept-Language': 'en-US,en;q=0.8',
       	'Connection': 'keep-alive'
	}
	source = urllib2.Request('http://ubuntupodcast.org/feed/podcast', headers=hdr)
	source = urllib2.urlopen(source)
	return source.read()

# function for getting all the CLLs from the website
# should be normally used when there is a back log
def get_all():
	root = lxml.etree.fromstring(get_source())
	code = root.xpath('*//content:encoded', namespaces={
		'content':'http://purl.org/rss/1.0/modules/content/',
	})

	for x in range(0,len(code)):
		cll = html.fromstring(code[x].text)
		cll = cll.xpath('*//code')
		try:
			clls.append(cll[0].text) # TODO - what if there are multiples in episode???
		except IndexError:
			print()
	return clls

# a function for getting only the latest CLL and outputs
# a singular element that can be ammended to an existing
# page of CLLs
def get_latest():
	root = lxml.etree.fromstring(get_source())
	code = root.xpath('*//content:encoded', namespaces={
		'content':'http://purl.org/rss/1.0/modules/content/',
	})
	cll = html.fromstring(code[0].text)
	cll = cll.xpath('*//code')
	clls.append(cll[0].text)
	return clls

# if you have a date of a particular podcast (or range of
# dates) then this function will iterate over that range and
# generate an output of the CLLs that appear within that sequence
def get_particular(url):
	return

print(get_all())
