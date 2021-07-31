from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import *
from users.models import *
from .forms import *

@login_required
def task_list(request):
		tasks = Task.objects.filter(user=request.user)
		categoties = Category.objects.filter(user=request.user)
		search_input = request.GET.get('search_area')
		if search_input:
			tasks = Task.objects.filter(title__startswith=search_input)
			context = {'tasks':tasks}
		else:
			tasks = Task.objects.filter(user=request.user)
			task_count = Task.objects.filter(complete=False).count()
			categoties = Category.objects.filter(user=request.user)
		context = {'tasks':tasks,'categoties':categoties, 'task_count':task_count}
		return render(request, 'todolist/task_list.html', context)


@login_required
def task_detail(request, task_id):
	try:
		task=Task.objects.get(id=task_id)
	except Task.DoesNotExist:
		raise Http404("Задачи не существует")
	context={'task':task}
	return render(request,'todolist/task_detail.html',context)


@login_required
def create_task(request):
	tasks = Task.objects.filter(user=request.user)
	if request.user.profile.sum_task >= 10 and not request.user.profile.tarif_pro:
		# return redirect('change_tarif')
		return render(request, 'users/payment.html')
	profile = request.user.profile
	form = TaskForm()
	if request.method == 'POST':
		form = TaskForm(request.POST)
		if form.is_valid():
			task = form.save(commit = False)
			task.user=request.user
			task.save()
			return redirect('task_list')	
	context = {'form':form}
	return render(request, 'todolist/create_task.html', context)



def edit_task(request,task_id):
	task = get_object_or_404(Task, id=task_id)
	if task.user == request.user:
		form = TaskForm(request.POST or None, instance = task)
		context = {'form':form}
		if form.is_valid():
			task=form.save()
			task.save()
			messages.success(request, 'Успешно обновлено')
			context = {'form':form}
			return redirect('task_list')
		else:
			context = {'form':form, 'error':'К сожалению, не обновлено. Повторите, пожалуйста.'}
			return render(request, 'todolist/edit_task.html', context)
	else:
		return redirect('login')


def delete_task(request,task_id):
	task= get_object_or_404(Task, id=task_id)
	if task.user == request.user:
		if request.method == "POST": 
			task.delete()
			messages.success(request, 'Успешно удалено!')
			return redirect('task_list')
		context= {'task':task}
		return render(request, 'todolist/delete_task.html', context)
	else:
		return redirect('login')


@login_required
def category_list(request):
	categories = Category.objects.all()
	context = {'categories':categories}
	return render(request, 'todolist/category_list.html', context)


@login_required
def category_create(request):
	categories = Category.objects.filter(user=request.user)
	context = {'categories':categories}
	form = CategoryForm()
	if request.method == 'POST':
		form = CategoryForm(request.POST)
		if form.is_valid():
			category = form.save(commit = False)
			category.user=request.user
			category.save()
			return redirect('category_list')	
	context = {'form':form}
	return render(request,'todolist/category_create.html', context)


def category_edit(request,cat_id):
	category = get_object_or_404(Category, id=cat_id)
	if category.user == request.user:
		form = CategoryForm(request.POST or None, instance = category)
		context = {'form':form}
		if form.is_valid():
			category=form.save()
			category.save()
			messages.success(request, 'Успешно обновлено')
			context = {'form':form}
			return redirect('category_list')
		else:
			context = {'form':form}
			return render(request, 'todolist/category_edit.html', context)
	else:
		return redirect('login')


def category_delete(request,cat_id):
	category= get_object_or_404(Category, id=cat_id)
	if category.user == request.user:
		if request.method == "POST": 
			category.delete()
			messages.success(request, 'Успешно удалено!')
			return redirect('category_list')
		context= {'category':category}
		return render(request, 'todolist/category_delete.html', context)
	else:
		return redirect('login')


# def subcategories(request,id):
# 	if request.method == 'POST':
# 		task = Task.objects.get(id=id)
# 		category = request.category
# 		form = SubcategoryForm(request.POST)
# 		if form.is_valid():
# 			form = form.save(commit=False)
# 			if request.POST.get('parent', None):
# 				form.parent_id = request.POST.get('parent')
# 			form.task = task
# 			form.category = category
# 			form.save()
# 			return redirect(task.get_absolute_url())
