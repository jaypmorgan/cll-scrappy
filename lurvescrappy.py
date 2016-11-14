#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import sys, argparse
import feedparser # pip install feedparser

clls = []

def get_source():
	feeds = feedparser.parse('http://ubuntupodcast.org/feed/podcast')
	for feed in feeds['entries']:
		cll_item = {}

		cll_item['item_title'] = feed['title']
		html_content = feed['content'][0]['value']

		soup = BeautifulSoup(html_content, 'html.parser')

		cll = []
		for commands in soup.find_all('code'):
			cll.append(commands.get_text())

		# if a cll argument was found in the podcast description
		if len(cll):
			cll_item['command'] = cll # add it to the array
			clls.append(cll_item) # then add it to the global dictionary

# function for getting all the CLLs from the website
# should be normally used when there is a back log
def get_all():
	items = get_source()
	print(clls)

# a function for getting only the latest CLL and outputs
# a singular element that can be ammended to an existing
# page of CLLs
def get_latest():
	code = get_source()
	print(clls[0])

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
