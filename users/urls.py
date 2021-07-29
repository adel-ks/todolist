from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import  static
from django.contrib.auth import views as auth_views 



urlpatterns = [
	path('register/', register, name='register'),
	path('login/', login, name='login'),
	path('logout/', logout, name='logout'),
	path('edit/', edit, name='edit'),
	# path('password_change/',auth_views.PasswordChangeView.as_view(template_name='users/password_change_form.html'), name='password_change'),
	path('password_change/',password_change, name='password_change'),
	path('password_change/done/', password_change_done, name='password_change_done'),
		
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)