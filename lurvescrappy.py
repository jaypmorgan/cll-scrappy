#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium import webdriver # pip install selenium
from datetime import datetime
import sys

if(len(sys.argv) == 1):
    print '\nUsage:'
    sys.exit()

# use the phantomjs web driver and load the ubuntu homepage
driver = webdriver.PhantomJS()
driver.get('http://ubuntupodcast.org')
assert "Ubuntu" in driver.title # has the page loaded

# function for getting all the CLLs from the website
# should be normally used when there is a back log
def getall():
    return

# function for getting only the latest CLL and outputs
# a singular element that can be ammended to an existing
# page of CLLs
def getlatest():
    return

# if you have a date of a particular podcast (or range of
# dates) then this function will iterate over that range and
# generate an output of the CLLs that appear within that sequence
def getparticular():
    return
