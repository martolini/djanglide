from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from glide.core.profiles.models import Profile
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.contrib import auth

from glide.core.profiles.forms import OccupationForm, PhotoForm, ProfileForm
from glide.core.profiles.models import Occupation
from glide.core.models import City

@login_required
def be_local(request):
	profile = get_object_or_404(Profile, user=request.user)
	interests = get_interests_for_profile(profile)
	form = ProfileForm(instance=profile)
	if request.method == 'POST':
		form = ProfileForm(request.POST, request.FILES or None, instance=profile)
		if form.is_valid():
			if not profile.is_local():
				cleaned_data = form.cleaned_data
				# Change profile attributes.
				if cleaned_data['new_first_name'] != profile.user.first_name:
					profile.user.first_name = cleaned_data['new_first_name'].capitalize()
				if cleaned_data['new_last_name'] != profile.user.last_name:
					profile.user.last_name = cleaned_data['new_last_name'].capitalize()
				if cleaned_data['new_email'] != profile.user.email:
					profile.user.email = cleaned_data['new_email']
				profile.user.save()

				# Change profile attributes.
				if cleaned_data['about'] != profile.about:
					profile.about = cleaned_data['about']
				if cleaned_data['birthday'] != profile.birthday:
					profile.birthday = cleaned_data['birthday']
				if cleaned_data['photo'] != profile.photo:
					profile.photo = cleaned_data['photo']
				if cleaned_data['country'] != profile.country:
					profile.country = cleaned_data['country']
				if cleaned_data['state'] != profile.state:
					profile.state = cleaned_data['state']
				if cleaned_data['gender'] != profile.gender:
					profile.gender = cleaned_data['gender']
				profile.save()

				# Change profile city.
				try:
					city = City.objects.get(name__iexact=cleaned_data['new_city'])
					city_created = False
				except:
					city = City(name=cleaned_data['new_city'].capitalize())
					city.save()
					city_created = True

				if city != profile.city:
					if city_created:
						if profile.state:
							city.state = profile.state
						if profile.country:
							city.country = profile.country
					profile.city = city
					profile.save()
				if not profile.city.has_local:
					profile.city.has_local = True
					profile.city.save()
			else:
				city = profile.city
				if len(Profile.objects.filter(city=city)) == 1:
					city.has_local = False
			profile.local = not profile.is_local()
			profile.save()
			return redirect(profile)
	return render(request,'profiles/local.html',{'profile': profile,
												 'form': form,
												 'interests': interests,
												})


def auth_view(request):
	if not request.POST:
		return HttpResponseRedirect('/')
	username = request.POST['username']
	password = request.POST['password']
	user = auth.authenticate(username=username, password=password)
	if user is not None and user.is_active:
			auth.login(request, user)
			try:
				return redirect(Profile.objects.get(user=user))
			except:
				pass
	return HttpResponseRedirect('/')


def logout(request):
	auth.logout(request)
	return HttpResponseRedirect('/')

def account(request):
	profile = get_object_or_404(Profile, user=request.user)
	return redirect(profile)

def get_interests_for_profile(profile):
	try:
		return profile.interest_set.all().order_by('name')
	except:
		return None

def get_occupation_for_profile(profile):
	try:
		return profile.occupation_set.all()[0]
	except:
		return None

# User visits some profile
def view_profile(request, username=False):
	profile = get_object_or_404(Profile, user__username=username)
	interests = get_interests_for_profile(profile)
	occupation = get_occupation_for_profile(profile)

	return render(request, 'profiles/view.html',
							{'profile': profile,
							'interests': interests,
							'occupation': occupation})

@login_required
def add_occupation(request):
	if request.method == 'POST':
		form = OccupationForm(request.POST)
		if form.is_valid():
			item = form.save(commit=False)
			profile = get_object_or_404(Profile, user=request.user)

			try:
				item = Occupation.objects.get(name__iexact=item.name)
			except:
				item.name = item.name.capitalize()
				item.save()

			try:
				occupation = profile.occupation_set.all()[0]
				occupation.profiles.remove(profile)
				occupation.save()
			except:
				pass

			item.profiles.add(profile)
			item.save()

			return redirect(profile)

@login_required
def add_photo(request):
	if request.method == 'POST':
		form = PhotoForm(request.POST, request.FILES)
		if form.is_valid():
			item = form.save(commit=False)
			profile = get_object_or_404(Profile, user=request.user)
			profile.photo = item.photo
			profile.save()
			return redirect(profile)

@login_required
def edit_profile(request):
	profile = get_object_or_404(Profile, user=request.user)
	form = ProfileForm(instance=profile)
	if request.method == 'POST':
		form = ProfileForm(request.POST, request.FILES or None, instance=profile)
		if form.is_valid():
			cleaned_data = form.cleaned_data

			# Change user attributes.
			if cleaned_data['new_first_name'] != profile.user.first_name:
				profile.user.first_name = cleaned_data['new_first_name'].capitalize()
			if cleaned_data['new_last_name'] != profile.user.last_name:
				profile.user.last_name = cleaned_data['new_last_name'].capitalize()
			if cleaned_data['new_email'] != profile.user.email:
				profile.user.email = cleaned_data['new_email']
			profile.user.save()

			# Change profile attributes.
			if cleaned_data['about'] != profile.about:
				profile.about = cleaned_data['about']
			if cleaned_data['birthday'] != profile.birthday:
				profile.birthday = cleaned_data['birthday']
			if cleaned_data['photo'] != profile.photo:
				profile.photo = cleaned_data['photo']
			if cleaned_data['country'] != profile.country:
				profile.country = cleaned_data['country']
			if cleaned_data['state'] != profile.state:
				profile.state = cleaned_data['state']
			if cleaned_data['gender'] != profile.gender:
				profile.gender = cleaned_data['gender']
			profile.save()

			# Change profile occupation.
			if cleaned_data['new_occupation'] != '':
				try:
					occupation = Occupation.objects.get(name__iexact=cleaned_data['new_occupation'].capitalize())
				except:
					occupation = Occupation(name=cleaned_data['new_occupation'].capitalize())
					occupation.save()

				if not profile in occupation.profiles.all():
					try:
						temp_occupation = profile.occupation_set.all()[0]
						temp_occupation.profiles.remove(profile)
						temp_occupation.save()
					except:
						occupation.profiles.add(profile)
						occupation.save()
			else:
				try:
					temp_occupation = profile.occupation_set.all()[0]
					temp_occupation.profiles.remove(profile)
					temp_occupation.save()
				except:
					pass

			# Change profile city.
			try:
				city = City.objects.get(name__iexact=cleaned_data['new_city'])
				city_created = False
			except:
				city = City(name=cleaned_data['new_city'].capitalize())
				city.save()
				city_created = True

			if city != profile.city:
				if city_created:
					if profile.state:
						city.state = profile.state
					if profile.country:
						city.country = profile.country
				city.save()
				profile.city = city
				profile.save()
			return redirect(profile)
	try:
		occupation = profile.occupation_set.all()[0]
	except:
		occupation = 'No occupation'
	return render(request, 'profiles/form.html', {'form':form,
												'profile': profile,
												'occupation': occupation})
