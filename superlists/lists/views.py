from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home_page (request):
	# print (type(HttpResponse('<html>')))
	# return HttpResponse('<html>')
	# return HttpResponse('<html><title>To-do lists</title>')
	# return HttpResponse('<html><title>To-Do lists</title></html>')
	# return HttpResponse('<html><title>To-Do lists</title><h1>To-Do</h1></html>')
	
	# Refactoring after functional test upgrade
	return render(request, 'home.html')