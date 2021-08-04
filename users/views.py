from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .decorators import *
from .models import Profile
from .forms import LoginForm, UserRegistrationForm, UserEditForm, ProfileEditForm
from .forms import *

@login_required
def my_profile(request):
	profile = Profile.objects.filter(user=request.user)
	context = {'profile': profile}
	return render(request, 'users/my_profile.html', context)


def register(request):
	if request.method == 'POST':
		user_form = UserRegistrationForm(request.POST)
		if user_form.is_valid():
			new_user = user_form.save(commit=False)
			new_user.set_password(user_form.cleaned_data['password'])
			new_user.save()
			
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


@login_required
def edit(request):
	if request.method == 'POST':
		user_form = UserEditForm(instance=request.user, data=request.POST)
		profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST, files=request.FILES)
		if user_form.is_valid() and profile_form.is_valid():
			user_form.save()
			profile_form.save()
			return redirect('my_profile')
	else:
		user_form = UserEditForm(instance=request.user)
		profile_form = ProfileEditForm(instance=request.user.profile)
		context = {'user_form': user_form, 'profile_form': profile_form}
		return render(request,'users/edit.html', context)
					  

@login_required
def tarif_pro(request):
	profile = request.user.profile
	if profile.tarif_pro == False:
		profile.tarif_pro = True
		profile.save()
	else:
		return HttpResponse("У вас уже есть премиум статус")
	return redirect("task_list")
