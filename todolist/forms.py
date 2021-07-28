from django import forms
from django.contrib.auth.models import User
from .models import Task, Category


class CategoryForm(forms.ModelForm):
	class Meta:
		model = Category
		fields = ['name',]
		

class TaskForm(forms.ModelForm):
	class Meta:
		model = Task
		fields = [
			'category',
			'title',
			'priority',
			'description',
			'complete',
		]

# class SubcategoryForm(forms.ModelForm):
# 	class Meta:
# 		model = Subcategory
# 		fields = [
# 			'name',
# 			'category',
# 			'task',
# 			'parent',
# 		]
