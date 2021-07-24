from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('todolist.urls')),
    # path('', include('social_django.urls', namespace='social')),
    # path('accounts/', include('allauth.urls')),
]

