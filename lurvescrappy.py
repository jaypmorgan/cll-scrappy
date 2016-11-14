#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime
from lxml import etree, html
import dateutil.relativedelta
import sys, argparse
import urllib2
from xml.etree import ElementTree as etree
import lxml.etree

import feedparser # pip install feedparser

clls = []

def get_source():
	feed = feedparser.parse('http://ubuntupodcast.org/feed/podcast')
	print(feed)
	print(feed['feed']['item'])


# this function is designed to return an array of command, description, and episode
# that the command is mentioned in. The input for this is the episode RSS feed.
def get_command(feed):
	source = html.fromstring(feed)
	feed_content = source.xpath('*//content:encoded', namespaces={
		'content':'http://purl.org/rss/1.0/modules/content/',
	})

	print(feed_content)

	commands = feed_content.xpath('*//code/text()')
	description = feed_content.xpath('*//code/../text()')

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
	items = get_source()
	print(items[0].text)

	for x in range(0,len(items)):
		# print(items[x].text)
		cll = get_command(items[x].text)
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
