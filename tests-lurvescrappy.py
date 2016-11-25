#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
import lurvescrappy
import rssfeeds # includes the test rss feed for test_get_command

class TestScrappyMethods(unittest.TestCase):
	def test_get_source(self):
		code = lurvescrappy.get_source()
		self.assertEqual(code[0].tag, '{http://purl.org/rss/1.0/modules/content/}encoded')

	def test_get_all(self):
		clls = lurvescrappy.get_all()
		print(clls[-1])
		self.assertEqual(clls[-1][0][0], 'speedtest-cli\n') # is the last element the same as always

	def test_get_latest(self):
		cll = lurvescrappy.get_latest()
		self.assertEqual(cll[0][0][0], 'nmtui') # needs a better test as it will fail when a new podcast is released

	def test_get_command(self):
		cll = lurvescrappy.get_command(rssfeeds.test_item)

if __name__ == '__main__':
	suite = unittest.TestLoader().loadTestsFromTestCase(TestScrappyMethods)
	unittest.TextTestRunner(verbosity=2).run(suite)
