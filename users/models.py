from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from PIL import Image
from django_resized import ResizedImageField



def user_image_dir(instance, filename):
	return os.path.join('fotos', f'{instance.user.id}', filename)


class Profile(models.Model):
	user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
	photo = ResizedImageField(size=[100,100], upload_to=user_image_dir, blank=True, null=True)
	tarif_pro = models.BooleanField(default=False)
	sum_task = models.IntegerField(default=False, null=True, editable=False)

	def __str__(self):
		return 'Профиль для пользователя {}'.format(self.user.username)

	# def create_profile(sender, instance, created, **kwargs):
	# 	if created:
	# 		Profile.objects.create(user=instance)
	# 		task_save.connect(create_profile, sender=User)

