from django.contrib import admin

# Register your models here.

from .models import TodoItem, Event

admin.site.register(TodoItem)
admin.site.register(Event)