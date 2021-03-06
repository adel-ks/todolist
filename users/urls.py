from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import  static
from django.contrib.auth import views as auth_views 



urlpatterns = [
	path('register/', register, name='register'),
	path('login/', login, name='login'),
	path('logout/', logout, name='logout'),
	path('my_profile/', my_profile, name='my_profile'),
	path('edit/', edit, name='edit'),
	path('tarif_pro/', tarif_pro, name='tarif_pro'),
	path('password_reset/', auth_views.PasswordResetView.as_view(template_name='users/password_reset_form.html', html_email_template_name='users/password_reset_email.html', subject_template_name='users/password_reset_subject.txt'), name = 'password_reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(template_name = "users/password_reset_done.html"), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name = 'users/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name = 'users/password_reset_complete.html'), name='password_reset_complete'),
]


