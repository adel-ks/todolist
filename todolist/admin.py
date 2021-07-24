from django.contrib import admin
from .models import *


class TaskAdmin(admin.ModelAdmin):
	list_display = ('profile','category','title','priority','complete')
	list_filter = ('category','priority','complete','created')
	search_fields = ('title','description')
	raw_id_fields = ('profile',)
	date_hierarchy = 'created'
	ordering = ['complete','created']


admin.site.register(Profile)
admin.site.register(Category)
admin.site.register(Task, TaskAdmin)
admin.site.register(Subcategory)
