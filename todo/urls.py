from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('todolist.urls')),
    path('', include('users.urls')),
    path('', include('social_django.urls', namespace='social')),
    path('accounts/', include('allauth.urls')),
    
]

