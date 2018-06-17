from django.shortcuts import render, HttpResponse
from tasks.models import ToDoTask, status_choices
from django.contrib.auth.models import AnonymousUser
from django.contrib.auth.decorators import login_required

import simplejson


color_code = {'stuck': '#c5c0bf',
			  'in progress': '#529fff',
			  'canceled': '#ffea54',
			  'done': '#7fdc7d'}

@login_required
def index(request):
	status = [x[0] for x in status_choices]
	tasks = ToDoTask.objects.filter(project__user=request.user).order_by('-status')
	default_task = 'stuck'
	for task in tasks:
		task.color = color_code[task.status]
	return render(request, 'index.html', locals())

def add_task(request, taskname):
	if taskname and not isinstance(request.user, AnonymousUser):
		print(request.user)
		obj = ToDoTask(user=request.user, name=taskname, priority=0, note='', status='stuck')
		obj.save()
		return HttpResponse(obj.id)
	return HttpResponse('FAIL')

def remove_task(request, id):
	try:
		task = ToDoTask.objects.get(id=int(id))
		task.delete()
		return HttpResponse('OK')
	except ToDoTask.DoesNotExist:
		return HttpResponse('FAIL')

def set_status(request, id, status):
	try:
		task = ToDoTask.objects.get(id=int(id))
		if status in (x[0] for x in status_choices):
			task.status = status
			task.save()
			data = {'result': 'OK', 'color':color_code[status]}
		else:
			data = {'result': 'NoStatus'}
	except Exception as ex:
		data = {'result': 'excetion', 'exception': ex}
	return HttpResponse(simplejson.dumps(data), content_type='application/json')
