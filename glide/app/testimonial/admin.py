from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from glide.app.testimonial.models import Testimonial

class TestimonialAdmin(ModelAdmin):
	list_display = ('user', 'author', 'date', 'rating')
	list_filter = ('user', 'author', 'date')

admin.site.register(Testimonial, TestimonialAdmin)