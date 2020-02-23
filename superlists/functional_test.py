from selenium import webdriver
import unittest

# browser = webdriver.Firefox()
# browser.get('http://localhost:8000')

# assert 'To-Do' in browser.title

class FunctionalTest(unittest.TestCase):
	"""docstring for FunctionalTest"""
	def setUp(self):
		self.browser = webdriver.Firefox()

	def tearDown(self):
		self.browser.quit()
	#User wants to visit the website
	def test_landing_page(self):
		self.browser.get('http://localhost:8000')
		self.assertIn('To-do lists', self.browser.title)
		# self.fail('Complete this test before moving onto something else')

if __name__ == '__main__':
	unittest.main()