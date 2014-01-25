from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from glide.app.contact.models import Improvement

class ImprovementAdmin(ModelAdmin):
	list_display = ('title', 'date', 'solved')
	list_filter = ('solved',)

admin.site.register(Improvement, ImprovementAdmin)
