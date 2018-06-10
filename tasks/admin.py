from django.contrib import admin
from tasks.models import ToDoTask

class ToDoTaskAdmin(admin.ModelAdmin):
	list_display = ('name', 'status', 'user')

admin.site.register(ToDoTask, ToDoTaskAdmin)