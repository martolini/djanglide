from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from glide.core.profiles.models import Profile, Occupation

class ProfileAdmin(ModelAdmin):
	list_display = ('user', 'birthday', 'country', 'state', 'city')
	list_filter = ('country', 'state', 'city', 'validated')
	search_filter = ('user',)

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Occupation)