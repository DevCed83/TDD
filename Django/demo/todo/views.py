from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from .models import TodoItem
from .forms import ItemForm
# Create your views here.
def index (request):
	item_list = TodoItem.objects.order_by('id')
	form = ItemForm()
	print (item_list)
	context = {'item_list' : item_list, 'form' : form}
	return render (request, 'todo/index.html', context)

@require_POST
def add_item(request):
	form = ItemForm(request.POST)
	print (request.POST['text'])

	if form.is_valid():
		new_item = TodoItem(text = request.POST['text'])
		new_item.save()	
	# forced refresh due to django use
	return redirect('index')
