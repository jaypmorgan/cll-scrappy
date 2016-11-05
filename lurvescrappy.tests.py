import unittest
import lurvescrappy

class TestScrappyMethods(unittest.TestCase):
	def test_get_source(self):
		code = lurvescrappy.get_source()
		self.assertEqual(code[0].tag, '{http://purl.org/rss/1.0/modules/content/}encoded')

	def test_get_all(self):
		clls = lurvescrappy.get_all()
		self.assertEqual(clls[-1], 'speedtest-cli\n') # is the last element the same as always

	def test_get_latest(self):
		cll = lurvescrappy.get_latest()
		self.assertEqual(cll[0], 'nmtui') # needs a better test as it will fail when a new podcast is released

if __name__ == '__main__':
	suite = unittest.TestLoader().loadTestsFromTestCase(TestScrappyMethods)
	unittest.TextTestRunner(verbosity=2).run(suite)
