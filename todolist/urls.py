from django.urls import path
from .views import *


urlpatterns = [
	# path('login/', login, name='login'),
	# path('logout/', logout, name='logout'),
	# path('register/', register, name='register'),
	# path('search_task/', search_task, name='search_task'),
	path('',task_list, name='tasks'),
	path('todolist/<id>/', task_detail, name='task'),
	path('create', create_task, name='create_task'),
	path('<int:task_id>/', edit_task, name='edit_task'),
	path('<int:task_id>/delete', delete_task, name='delete_task'),
]
