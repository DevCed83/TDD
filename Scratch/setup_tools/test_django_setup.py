import unittest
import os
class test_django_setup(unittest.TestCase):
	def setUp(self):
		pass
	def tearDown(self):
		pass
	def test_django_version(self):
			self.assertTrue(type(os.system('django-admin version')), 'class <str>')

if __name__ == '__main__':
	unittest.main()