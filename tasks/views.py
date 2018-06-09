from django.shortcuts import render, HttpResponse
from tasks.models import ToDoTask, status_choices
from django.contrib.auth.models import AnonymousUser



def index(request):
	color_code = {'stuck': '#ea4e4e',
				  'in progress': '#7fdc7d',
				  'canceled': '#ffea54',
				  'done': '#529fff'}
	status = [x[0] for x in status_choices]
	tasks = ToDoTask.objects.order_by('id')
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
			return HttpResponse('OK')
		else:
			return HttpResponse('NoStatus')
	except Exception as ex:
		return HttpResponse(ex)
