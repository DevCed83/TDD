from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home_page (request):
	# print (type(HttpResponse('<html>')))
	# return HttpResponse('<html>')
	# return HttpResponse('<html><title>To-do lists</title>')
	return HttpResponse('<html><title>To-do lists</title></html>')