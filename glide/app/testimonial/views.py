from django.contrib.auth.decorators import login_required
from glide.app.testimonial.forms import TestimonialForm
from glide.app.testimonial.models import Testimonial
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from glide.core.profiles.models import Profile
from django.http import HttpResponsePermanentRedirect
from glide.core.notifications.views import new_notification
@login_required
def add(request, username):
	user = get_object_or_404(User, username=username)
	profile = get_object_or_404(Profile, user=user)
	form = TestimonialForm()
	if request.method == 'POST':
		form = TestimonialForm(request.POST)
		if form.is_valid():
			item = form.save(commit=False)
			item.rating = get_rating(request.POST)
			item.author = request.user
			item.user = user
			item.save()
			new_notification("review",user,request.user)
			return HttpResponsePermanentRedirect(profile.get_absolute_url())
	return render(request, 'testimonial/form.html', {'form':form,
													'profile':profile})
def get_rating(POST):
	try:
		if POST['rating-input-5']:
			return 5
	except:
		pass
	try:
		if POST['rating-input-4']:
			return 4
	except:
		pass
	try:
		if POST['rating-input-3']:
			return 3
	except:
		pass
	try:
		if POST['rating-input-2']:
			return 2
	except:
		pass
	try:
		if POST['rating-input-1']:
			return 1
	except:
		pass
	return 0