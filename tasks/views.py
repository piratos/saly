from django.shortcuts import render
from tasks.models import ToDoTask



def index(request):
	color_code = {'stuck': '#ea4e4e',
				  'in progress': '#7fdc7d',
				  'canceled': '#ffea54',
				  'done': '#529fff'}
	tasks = ToDoTask.objects.order_by('id')
	for task in tasks:
		task.color = color_code[task.status]
	return render(request, 'index.html', locals())