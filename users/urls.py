from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import  static



urlpatterns = [
	path('login/', login, name='login'),
	path('logout/', logout, name='logout'),
	path('register/', register, name='register'),
	path('edit/', edit, name='edit'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)