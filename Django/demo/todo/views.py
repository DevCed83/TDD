from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from .models import TodoItem, Event
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
	create_event('add item')
	return redirect('index')

def complete_item(request, item_id):
	item = TodoItem.objects.get(pk = item_id)
	item.complete = False if item.complete else True
	item.save()
	create_event('toggle item complete state')
	return redirect('index')

def delete_completed(request):
	items = TodoItem.objects.filter(complete__exact = True)
	items.delete()
	create_event('delete completed')
	return redirect('index')

def clear_all(request):
	items = TodoItem.objects.all()
	items.delete()
	create_event('clear_all')
	return redirect('index')

def create_event(view_name):
	event = Event()
	event.nature = 'test click'
	event.event = view_name
	event.save()

