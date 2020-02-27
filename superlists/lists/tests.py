from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string
from views import home_page

# Create your tests here.
class HomePageTest(TestCase):
	"""docstring for SmokeTest"""

	def test_url_to_view(self):
		found = resolve('/')
		self.assertEqual(found.func, home_page)

	def test_view_to_template(self):
		response = self.client.get('/')
		html = response.content.decode('utf-8')
		self.assertTrue(html.startswith('<html>'))
		self.assertIn('<title>To-Do lists</title>', html)
		self.assertTrue(html.strip().endswith('</html>'))
		# expected_html = render_to_string('home.html')
		# self.assertEqual(html, expected_html)
		self.assertTemplateUsed(response, 'homes.html')
		# self.fail('Complete this test before moving onto something else')

	