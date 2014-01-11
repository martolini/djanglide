from django.template.base import Library
from glide.app.testimonial.forms import TestimonialForm
from glide.app.testimonial.models import Testimonial

register = Library()

@register.inclusion_tag('testimonial/templatetags/list.html', takes_context=True)
def load_testimonials(context, profile):
	testimonials = Testimonial.objects.filter(user=profile.user).order_by('date')
	return {'MEDIA_URL':context['MEDIA_URL'], 'STATIC_URL':context['STATIC_URL'], 'testimonials':testimonials}
