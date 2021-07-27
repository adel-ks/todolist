from django.contrib import admin
from .models import *
from users.models import *


class TaskAdmin(admin.ModelAdmin):
	list_display = ('user','category','title','priority','complete')
	list_filter = ('category','priority','complete','created')
	search_fields = ('title','description')
	raw_id_fields = ('user',)
	date_hierarchy = 'created'
	ordering = ['complete','created']

class ProfileAdmin(admin.ModelAdmin):
	list_display = ('user', 'photo', 'tarif_pro')


admin.site.register(Profile, ProfileAdmin)
admin.site.register(Category)
admin.site.register(Task, TaskAdmin)
# admin.site.register(Subcategory)
