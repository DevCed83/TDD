from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home_page (request):
	# print (type(HttpResponse('<html>')))
	# return HttpResponse('<html>')
	# return HttpResponse('<html><title>To-do lists</title>')
	# return HttpResponse('<html><title>To-Do lists</title></html>')
	# return HttpResponse('<html><title>To-Do lists</title><h1>To-Do</h1></html>')
	# test the request method to handle POST request
	if request.method == 'POST':
		#response = HttpResponse(request.POST['item-text'])
		# return render(request, 'home.html', {'new_item_text' : 'A new list item'})
		return render (request, 'home.html', {'new_item_text':request.POST.get('item_text','')})
	# Refactoring after functional test upgrade
	return render(request,'home.html')