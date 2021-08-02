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

	def __init__(self, *args, **kwargs):
		print(kwargs)
		user = kwargs.pop('user', None)
		super(TaskForm, self).__init__(*args, **kwargs)
		self.fields['category'].queryset = Category.objects.filter(user=user)

