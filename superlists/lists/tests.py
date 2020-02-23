from django.test import TestCase
from django.urls import resolve
from lists.views import home_page

# Create your tests here.
class SmokeTest(TestCase):
	"""docstring for SmokeTest"""
	def test_root_url_resolves_home_page(self):
		found = resolve('/')
		self.assertEqual(found.func, home_page)		