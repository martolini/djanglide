from django.template.base import Library
from glide.app.booking.forms import BookForm
from django.db.models import Q

register = Library()

@register.inclusion_tag('booking/templatetags/book-form.html')
def load_book_form(profile):
	form = BookForm()
	return {'form':form,'profile':profile}