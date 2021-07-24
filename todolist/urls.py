from django.urls import path
from .views import *


urlpatterns = [
	path('',task_list, name='tasks'),
	path('todolist/<id>/', task_detail, name='task'),
	path('create', create_task, name='create_task'),
	path('<int:task_id>/', edit_task, name='edit_task'),
	path('<int:task_id>/delete', delete_task, name='delete_task'),
]
