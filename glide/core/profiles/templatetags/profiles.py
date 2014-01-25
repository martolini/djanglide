from django.template.base import Library
from glide.core.profiles.forms import OccupationForm, PhotoForm
from django.db.models import Sum
from glide.app.testimonial.models import Testimonial
from math import ceil

register = Library()

@register.inclusion_tag('profiles/templatetags/occupation-form.html')
def load_occupation_form():
	form = OccupationForm()
	return {'form':form}

@register.inclusion_tag('profiles/templatetags/photo-form.html')
def load_photo_form():
	form = PhotoForm()
	return {'form':form}

@register.inclusion_tag('profiles/templatetags/rating.html', takes_context=True)
def load_rating(context, profile):
	testimonials = Testimonial.objects.filter(user=profile.user)
	if testimonials.count() == 0:
		rating = 0
	else:
		total = testimonials.aggregate(Sum('rating'))['rating__sum']
		rating = ceil(float(total) / float(testimonials.count()))
	return {'STATIC_URL':context['STATIC_URL'], 'rating':rating}
