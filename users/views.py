from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Profile
from .forms import *
from .forms import LoginForm, UserRegistrationForm, UserEditForm, ProfileEditForm




@login_required
def register(request):
	if request.method == 'POST':
		user_form = UserRegistrationForm(request.POST or None)
		if user_form.is_valid():
			new_user = user_form.save(commit=False)
			new_user.set_password(user_form.cleaned_data['password'])
			new_user.save()
			profile = Profile.objects.create(user=new_user)
			context = {'new_user': new_user}
			return render(request, 'users/register_done.html', context)
	else:
		user_form = UserRegistrationForm()
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
				return redirect('task_list')
	context = {'form': form}
	return render(request, 'users/login.html', context)


def logout(request):
	auth_logout(request)
	return redirect('login')



@login_required(login_url='login')
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST, files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
        return render(request,
                      'users/edit.html',
                      {'user_form': user_form,
                       'profile_form': profile_form})