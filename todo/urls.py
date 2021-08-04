from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from pages.views import index



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name = 'index_page'),
    path('', include('todolist.urls')),
    path('', include('users.urls')),
    path('accounts/', include('allauth.urls')),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
