from django.template.base import Library
from glide.app.interests.forms import InterestForm

register = Library()

@register.inclusion_tag('interests/templatetags/form.html')
def load_interests_form():
	form = InterestForm()
	return {'form':form}