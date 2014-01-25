from django.forms.models import ModelForm
from glide.app.testimonial.models import Testimonial
from django.utils.translation import ugettext_lazy as _

class TestimonialForm(ModelForm):
	class Meta:
		model = Testimonial
		exclude = ('user', 'author', 'date', 'rating')




