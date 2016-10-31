#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium import webdriver # pip install selenium
from datetime import datetime
from lxml import etree, html
import dateutil.relativedelta
import sys, argparse, config, threading, chardet

date_now = datetime.now()
oldest_archive = datetime.strptime(config.oldest, '%Y-%m-%d')

# program description
parser = argparse.ArgumentParser(description="""Script for procedurally
getting the command line love arguments from the ubuntu podcast website.
The output of this script can be defined using optional flags
""")

# program flags
parser.add_argument('--all', dest='getall', help='get all the command line loves from the archives')
args = parser.parse_args()

#CLLs
clls = {}

def get_source():
	url_string = config.url + '/feed/podcast/'
	driver = webdriver.PhantomJS()
	driver.get(url_string)
	return str(driver.page_source.encode('ascii', 'ignore').strip())

# function for getting all the CLLs from the website
# should be normally used when there is a back log
def get_all():
	target_date = date_now
	date_list = []

	# we want to generate a list of URLs to crawl. We start with the current year
	# and month and work backwards to the oldest date (set in the config file)
	while(target_date > oldest_archive):
		url_string = str(target_date.year) + '/' + target_date.strftime('%m') + '/' # the url format is '/year/month/'
		date_list.append(url_string) # add this to the array of urls to be scrapped
		target_date = target_date - dateutil.relativedelta.relativedelta(months = 1) # take away another month

# a function for getting only the latest CLL and outputs
# a singular element that can be ammended to an existing
# page of CLLs
def get_latest():
	source = get_source()
	encoding = chardet.detect(source)['encoding']
	if encoding != 'utf-8':
		source = source.decode(encoding, 'replace').encode('utf-8')

	encode_source = etree.parse(source)
	return encode_source.xpath('/rss/channel')[0]

# if you have a date of a particular podcast (or range of
# dates) then this function will iterate over that range and
# generate an output of the CLLs that appear within that sequence
def get_particular(url):
	driver = webdriver.PhantomJS()
	driver.get(url)
	cll = driver.find_element_by_xpath('*//code').text
	print(cll)

print(get_latest())
