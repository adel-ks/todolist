from django.shortcuts import redirect

def for_authenticated_user(view_func):
	def wrapper_func(request, *args, **kwargs):
		if request.user.is_anonymous:
			return redirect('register')
		else:
			return view_func(request, *args, **kwargs)

	return wrapper_func