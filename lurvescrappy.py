#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime
from lxml import etree, html
import dateutil.relativedelta
import sys, argparse
import urllib2
from xml.etree import ElementTree as etree
import lxml.etree

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
	root = lxml.etree.fromstring(source.read())
	code = root.xpath('*//content:encoded', namespaces={
		'content':'http://purl.org/rss/1.0/modules/content/',
	})
	return code


# this function is designed to return an array of command, description, and episode
# that the command is mentioned in. The input for this is the episode RSS feed.
def get_command(feed):
	source = html.fromstring(feed)
	commands = source.xpath('*//code/text()')
	description = source.xpath('*//code/../text()')

	temp_clls = []

	for x in range(0, len(commands)):
		try:
			temp_clls.append([commands[x],' '.join(description)])
		except IndexError:
			pass

	return temp_clls

# function for getting all the CLLs from the website
# should be normally used when there is a back log
def get_all():
	code = get_source()

	for x in range(0,len(code)):
		cll = get_command(code[x].text)
		clls.append(cll)
	return clls

# a function for getting only the latest CLL and outputs
# a singular element that can be ammended to an existing
# page of CLLs
def get_latest():
	code = get_source()

	cll = get_command(code[0].text)
	clls.append(cll)
	return clls

# program description
parser = argparse.ArgumentParser(description="""Script for procedurally
getting the command line love arguments from the ubuntu podcast website.
The output of this script can be defined using optional flags
""")

# program flags
FUNCTION_MAP = {'all' : get_all,
                'latest' : get_latest }

parser.add_argument('command', choices=FUNCTION_MAP.keys())

args = parser.parse_args()

func = FUNCTION_MAP[args.command]
func()
