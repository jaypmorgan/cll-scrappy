#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import sys, argparse
import feedparser # pip install feedparser
import json

clls = []
output = []

def get_source():
	feeds = feedparser.parse('http://ubuntupodcast.org/feed/podcast')
	for feed in feeds['entries']:
		cll_item = {}

		cll_item['title'] = feed['title']
		cll_item['url'] = feed['link']
		html_content = feed['content'][0]['value']

		soup = BeautifulSoup(html_content, 'html.parser')

		cll = []
		for commands in soup.find_all('code'):
			cll.append(commands.get_text())

		# if a cll argument was found in the podcast description
		if len(cll):
			cll_item['command'] = cll # add it to the array
			clls.append(cll_item) # then add it to the global dictionary

# program description
parser = argparse.ArgumentParser(description="""Script for procedurally
getting the command line love arguments from the ubuntu podcast website.
The output of this script can be defined using optional flags
""")

parser.add_argument('state', choices=['all', 'latest'], nargs='?')

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

def print_html():
	output_string = "<table><tr>"
	for key, value in clls[0].iteritems():
		output_string += "<th>"
		output_string += key
		output_string += "</th>"
	output_string += "</tr>"
	for cll in output:
		output_string += "<tr><td>"
		for command in cll['command']:
			output_string += command
		output_string += "</td><td>"
		output_string += cll['title']
		output_string += "</td></tr>"

	output_string += "</table>"
	output_string = output_string.encode('ascii', 'ignore')
	return output_string

def print_json():
	output_string = json.dumps(clls)
	output_string = output_string.encode('ascii', 'ignore')
	return output_string

selected_command = str(args.state)
if selected_command == 'all':
	output = clls
elif selected_command == 'latest':
	output = [clls[0]]
else:
	output = clls

if args.output:
	f = open(args.output, 'w')
	if args.json:
		print >> f, print_json()
	elif args.html:
		print >> f, print_html()
	else:
		print >> f, output
	f.close()
else:
	if args.json:
		print(print_json())
	elif args.html:
		print(print_html())
	else:
		print(output)
