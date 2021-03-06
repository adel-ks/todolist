# Generated by Django 3.2.5 on 2021-08-04 10:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_resized.forms
import users.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', django_resized.forms.ResizedImageField(blank=True, crop=None, default='default.png', force_format=None, keep_meta=True, null=True, quality=0, size=[400, 400], upload_to=users.models.user_image_dir)),
                ('tarif_pro', models.BooleanField(default=False)),
                ('sum_task', models.IntegerField(default=False, editable=False, null=True)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
