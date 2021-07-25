from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required


def task_list(request):
	tasks = Task.objects.all()
	categoties = Category.objects.all()
	context = {'tasks':tasks, 'categoties':categoties}
	search_input = request.GET.get('search_area')
	if search_input:
		tasks = Task.objects.filter(title__startswith=search_input)
		categoties = Task.objects.filter(title__startswith=search_input)
		context = {'tasks':tasks,'categoties':categoties}
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


# def create_task(request):
# 	form = TaskForm()
# 	if request.method == 'POST':
# 		form = TaskForm(request.POST)
# 		if form.is_valid():
# 			form.save()
# 			return redirect('/')
# 	context = {'form':form}
# 	return render(request, 'todolist/create_task.html',context)


def create_task(request):
	sum_task = Profile.objects.all().values('sum_task')
	tasks = Task.objects.all()
	profile = request.user.profile
	form = TaskForm()
	if request.method == 'POST':
		form = TaskForm(request.POST)
		if form.is_valid():
			if request.user.profile.sum_task == 10 and request.user.profile.tarif_pro == False:
				messages.success(request, 'Перейти на тариф PRO')
				return HttpResponseRedirect('change_tarif')
			elif request.user.profile.tarif_pro == True:
				task = form.save(commit = False)
				task.user=request.user
				task.save()
				return redirect('task_list')
	context = {'form':form}
	return render(request, 'todolist/create_task.html',context)


def edit_task(request,task_id):
	task = get_object_or_404(Task, id=id)
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


def delete_task(request,id):
	task= get_object_or_404(Task, id=id)
	if request.method == "POST" and request.user.is_authenticated:
		task.delete()
		messages.success(request, 'Успешно удалено!')
		return HttpResponseRedirect('todolist/')
	
	context= {'task': task}
	
	return render(request, 'todolist/delete_task.html', context)


def category_list(request):
	categories = Category.objects.all()
	context = {'categories':categories}
	return render(request, 'todolist/category_list.html', context)


def category_create(request):
	form = CategoryForm()
	if request.method == 'POST':
		form = CategoryForm(request.POST)
		if form.is_valid():
			category = form.save(commit=False)
			category.user=request.user
			category.save()
	context = {'form':form}
	return render(request,'todolist/category_create.html', context)


def subcategories(request,id):
	if request.method == 'POST':
		task = Task.objects.get(id=id)
		category = request.category
		form = SubcategoryForm(request.POST)
		if form.is_valid():
			form = form.save(commit=False)
			if request.POST.get('parent', None):
				form.parent_id = request.POST.get('parent')
			form.task = task
			form.category = category
			form.save()
			return redirect(task.get_absolute_url())
