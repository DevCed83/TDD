from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string
from lists.views import home_page

# Create your tests here.
class HomePageTest(TestCase):
	"""docstring for SmokeTest"""

	def test_url_to_view(self):
		found = resolve('/')
		self.assertEqual(found.func, home_page)

	def test_view_to_template(self):
		request = HttpRequest()
		response = home_page(request)
		html = response.content.decode('utf-8')
		# self.assertTrue(html.startswith('<html>'))
		# self.assertIn('<title>To-Do lists</title>', html)
		# self.assertTrue(html.endswith('</html>'))
		expected_html = render_to_string('home.html')
		self.assertEqual(html, expected_html)
		# self.fail('Complete this test before moving onto something else')

	