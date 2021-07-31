from django.urls import path, include
from .views import *


urlpatterns = [
	path('tasks/',task_list, name='task_list'),
	path('tasks/<int:id>/', task_detail, name='task'),
	path('tasks/create/', create_task, name='create_task'),
	path('tasks/edit/<int:task_id>/', edit_task, name='edit_task'),
	path('tasks/delete/<int:task_id>/', delete_task, name='delete_task'),
	# path('change_tarif/', change_tarif, name='change_tarif'),
	path('categories/', category_list, name = 'category_list'),
	path('categories/create', category_create, name='category_create'),
	path('categories/<int:cat_id>/', category_edit, name='category_edit'),
	path('categories/<int:cat_id>/delete/', category_delete, name='category_delete'),
]
