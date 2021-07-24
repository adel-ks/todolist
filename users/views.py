from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from .forms import LoginForm, RegistrationForm 
from django.contrib.auth.models import User



def register(request):
	if request.method == 'POST':
		user_form = RegistrationForm(request.POST or None)
		if user_form.is_valid():
			new_user = user_form.save()
			new_user.set_password(user_form.cleaned_data['password'])
			new_user.save()
			profile = Profile.objects.create(user=new_user)
			context = {'new_user': new_user}
			return render(request, 'users/register_done.html', context)
	else:
		user_form = RegistrationForm()
	context = {'user_form': user_form}  
	return render(request, 'users/register.html',context)


def login(request):
	form = LoginForm()
	if request.method == 'POST':
		form = LoginForm(data =request.POST)
		if form.is_valid():
			cd = form.cleaned_data

			user = authenticate(username = cd['username'], password = cd['password'])
			if user is not None:
				auth_login(request, user)
				return redirect('tasks')
	context = {'form': form}
	return render(request, 'users/login.html', context)


def logout(request):
	auth_logout(request)
	return redirect('login')

