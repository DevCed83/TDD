import unittest
from selenium import webdriver

class FunctionalTest(unittest.TestCase):
	def setUp(self):
		self.browser = webdriver.Firefox()
		self.domain = 'http://localhost:8000'

	def tearDown(self):
		self.browser.quit()

	def test_page_accueil(self):
		self.browser.get(self.domain)
		self.assertIn('Site Todo', self.browser.title)
		main_heading = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('Todo List', main_heading)
		input_box = self.browser.find_element_by_id('input_box')
		self.assertEqual('Enter todo e.g. Delete junk files', input_box.get_attribute('placeholder'))


if __name__ == '__main__':
	unittest.main()