from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django_resized import ResizedImageField


def user_image_dir(instance, filename):
	return os.path.join('fotos', f'{instance.user.id}', filename)


class Profile(models.Model):
	user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
	photo = ResizedImageField(size=[100,100], upload_to=user_image_dir, blank=True, null=True)
	is_status = models.BooleanField(default=False)
	sum_todo = models.IntegerField(default=False, null=True, editable=False)

	def __str__(self):
		return self.user

	def create_profile(sender, instance, created, **kwargs):
		if created:
			Profile.objects.create(user=instance)
			task_save.connect(create_profile, sender=User)


class Category(models.Model):
	name = models.CharField(max_length=150, null=True, verbose_name='Категория')

	def __str__(self):
		return self.name


class Task(models.Model):
	PRIORITY = [
	(1, 'Важные и срочные'),
	(2, 'Важные и несрочные'),
	(3, 'Неважные и несрочные'),
	]

	profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
	title = models.CharField(max_length=200, verbose_name='Название')
	category = models.ForeignKey(Category,on_delete=models.CASCADE, blank=True, null=True)
	priority = models.PositiveSmallIntegerField(blank=False, choices=PRIORITY, default=3, verbose_name='Приоритет')
	description = models.TextField(null=True, blank=True, verbose_name='Описание')
	complete = models.BooleanField(default=False, verbose_name='Выполнено')
	created = models.DateTimeField(auto_now_add=True)


	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('views.task_details', args=[str(self.id)])



	def get_subcategories(self):
		return self.subcategory_set.filter(parent__isnull=True)


	def save(self, *args, **kwargs):
		if self.profile.sum_todo < 11:
			self.profile.sum_todo +=1
			self.profile.save()
		super().save(*args, **kwargs)


	def delete(self, *args, **kwargs):
		super(Task, self).delete(*args, **kwargs)
		self.todo.delete()


	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['tasks'] = context['tasks'].filter(user=self.request.user)
		context['count'] = context['tasks'].filter(complete=False).count()
		return context

	class Meta:
		ordering = ['complete']



class Subcategory(models.Model):
	text = models.TextField(max_length=500)
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	task = models.ForeignKey(Task, on_delete=models.CASCADE)
	parent = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True)

	def __str__(self):
		return f'{self.category.name} - {self.task.name}'

	class Meta:
		verbose_name='Подкатегория'
		verbose_name_plural='Подкатегории'			