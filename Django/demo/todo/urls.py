from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name = 'index'),
	path('add', views.add_item, name = 'add'),
	path('complete_item/<item_id>', views.complete_item, name = 'toggle'),
	path('delete_completed', views.delete_completed, name = 'delete_completed'),
	path('clear_all', views.clear_all, name = 'clear_all'),
	]