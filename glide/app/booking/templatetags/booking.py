from django.template.base import Library
from glide.app.booking.forms import BookForm
from django.db.models import Q
from django.shortcuts import get_object_or_404
from glide.core.profiles.models import Profile
from glide.app.booking.models import BookRequest
register = Library()

@register.inclusion_tag('booking/templatetags/book-form.html')
def load_book_form(profile):
	form = BookForm()
	return {'form':form,'profile':profile}

@register.inclusion_tag('templatetags/bookrequests.html')
def load_bookings_request(user):
	profile = get_object_or_404(Profile, user=user)
	bookings = BookRequest.objects.filter(target_recipient=profile,response=None)
	return {'bookings':bookings}