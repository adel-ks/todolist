from django.shortcuts import render
from .models import *
from .forms import *

from django.contrib.auth.decorators import login_required

@login_required
def task_list(request):
	tasks = Task.objects.all()
	context = {'tasks': tasks}
	# return render(request, 'todolist/task_list.html', context)
	search_input = request.GET.get('search_area')
	if search_input:
		tasks = Task.objects.filter(title__startswith=search_input)
		context = {'tasks': tasks}
	else:
		tasks = Task.objects.all()
	context = {'tasks':tasks}
	return render(request, 'todolist/task_list.html', context)


def task_detail(request, id):
	try:
		task=Task.objects.get(id=id)
	except Task.DoesNotExist:
		raise Http404("Задачи не существует")
	context={'task':task,}
	return render(request,'todolist/task_detail.html',context)


def create_task(request):
	form = TaskForm()
	if request.method == 'POST':
		if request.user.profile.sum_todo == 10:
				redirect ('todolist/payment.html')
				form = TaskForm(request.POST)
				if form.is_valid():
					form.save()
				return redirect('/')
	context = {'form':form}
	return render(request, 'todolist/create_task.html',context)


def edit_task(request,task_id):
	task = get_object_or_404(Task, id = task_id)
	form = TaskForm(request.POST or None, instance = task)
	context = {'form':form}

	if form.is_valid():
		task=form.save()
		task.save()
		messages.success(request, 'Успешно обновлено')
		context = {'form':form}
		return render(request, 'todolist/task_list.html', context)
	else:
		context = {'form':form, 'error':'К сожалению, не обновлено. Повторите, пожалуйста.'}
	return render(request, 'todolist/edit_task.html', context)


def delete_task(request, task_id):
	task= get_object_or_404(Task, id=task_id)
	if request.method == "POST" and request.user.is_authenticated:
		task.delete()
		messages.success(request, 'Успешно удалено!')
		return HttpResponseRedirect('todolist/')
	
	context= {'task': task}
	
	return render(request, 'todolist/delete_task.html', context)