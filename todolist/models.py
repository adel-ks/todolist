from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


class Category(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	name = models.CharField(max_length=150, null=True, verbose_name='Название')

	def __str__(self):
		return self.name



class Task(models.Model):
	PRIORITY = [
	(1, 'Важные и срочные'),
	(2, 'Важные и несрочные'),
	(3, 'Неважные и несрочные'),
	]

	user = models.ForeignKey(User, on_delete=models.CASCADE)
	title = models.CharField(max_length=200, verbose_name='Название')
	category = models.ForeignKey(Category,on_delete=models.CASCADE, blank=True, null=True, verbose_name='Категория')
	priority = models.PositiveSmallIntegerField(blank=False, choices=PRIORITY, default=3, verbose_name='Приоритет')
	description = models.TextField(null=True, blank=True, verbose_name='Описание')
	complete = models.BooleanField(default=False, verbose_name='Выполнено')
	created = models.DateTimeField(auto_now_add=True)


	def __str__(self):
		return self.title


	def save(self, *args, **kwargs):
	  	self.user.profile.sum_task += 1
	  	self.user.profile.save()
	  	super().save(*args, **kwargs)



	def get_absolute_url(self):
		return reverse('views.task_details', args=[str(self.id)])


	
	class Meta:
		ordering = ['complete']


