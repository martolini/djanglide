from django.contrib.auth.decorators import login_required
from glide.app.interests.forms import InterestForm
from glide.app.interests.models import Interest
from glide.core.profiles.models import Profile
from django.shortcuts import render, get_object_or_404, redirect

@login_required
def add(request):
	if request.method == 'POST':
		form = InterestForm(request.POST)
		if form.is_valid():
			instance = form.save(commit=False)
			profile = Profile.objects.get(user=request.user)
			try:
				instance = Interest.objects.get(name__iexact=instance.name)
			except:
				instance.name = instance.name.capitalize()
				instance.save()
			instance.profiles.add(profile)
			instance.save()

			return redirect(profile)
		return redirect(Profile.objects.get(user=request.user))

@login_required
def delete(request, id):
	item = get_object_or_404(Interest, pk=id)
	profile = get_object_or_404(Profile, user=request.user)
	item.profiles.remove(profile)
	item.save()
	return redirect(profile)
