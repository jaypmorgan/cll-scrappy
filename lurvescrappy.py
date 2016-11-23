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

		cll_item['title'] = feed['title']
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
parser.add_argument('--html',
					help="output the clls as a html table",
					action="store_true")
parser.add_argument('--json',
					help="output the clls as a json format",
					action="store_true")
parser.add_argument('-o', '--output',
					help="specify an output file for the clls to be stored to")
args = parser.parse_args()

get_source()
if args.html:
	output_string = "<table><tr>"
	for key, value in clls[0].iteritems():
		output_string += "<th>"
		output_string += key
		output_string += "</th>"
	output_string += "</tr>"
	for cll in clls:
		output_string += "<tr><td>"
		for command in cll['command']:
			output_string += command
		output_string += "</td><td>"
		output_string += cll['title']
		output_string += "</td></tr>"

	output_string += "</table>"
	output_string = output_string.encode('ascii', 'ignore')

if args.json:
	# TODO add output_string in a json format

if args.output:
	f = open(args.output, 'w')
	if args.html:
		print >> f, output_string
	else:
		print >> f, clls
	f.close()
