from django.contrib.auth import authenticate, login
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext

from glide.core.profiles.forms import LandingRegistrationForm
from glide.core.profiles.models import Profile

def frontpage(request):
	try:
		if request.user.is_authenticated():
			example_profile = Profile.objects.filter(local=True).exclude(user=request.user).exclude(photo='').order_by('?')[0]
		else:
			example_profile = Profile.objects.filter(local=True).exclude(photo='').order_by('?')[0]
	except:
		example_profile = False

	form = LandingRegistrationForm()

	if request.method == 'POST':
		d = request.POST.copy()
		d.update({'password1': d.get('password'), 'password2': d.get('password')})
		form = LandingRegistrationForm(d)
		if form.is_valid():
			new_user = form.save()
			new_user = authenticate(username=request.POST['username'], password=request.POST['password'])
			login(request, new_user)

			try:
				return redirect(Profile.objects.get(user=new_user))
			except:
				pass
	return render_to_response('landing/base.html', {
		'example_profile':example_profile,
	    'form': form}, RequestContext(request))
