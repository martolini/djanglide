from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from glide.app.marketplace.forms import SearchForm
from glide.core.profiles.models import Profile
from glide.app.interests.models import Interest
from django.db.models import Q
from glide.core.models import City
from math import ceil

def marketplace(request):
	search_form = SearchForm()
	return render(request, 'marketplace/base.html', {'search_form':search_form})

def search(request):
	query = request.GET.get('query')
	form = SearchForm(query=query)
	hits = 0
	occupation_filter = []
	interest_filter = []
	results = None

	if query:
		results = Profile.objects.filter(local=True, city__id=query).order_by('user__first_name')
		hits = len(results)

	if hits:
		for result in results:
			interests = result.interest_set.all()
			occupations = result.occupation_set.all()
			
			for interest in interests:
				if interest.name not in interest_filter:
					interest_filter.append(interest.name)

			for occupation in occupations:
				if occupation.name not in occupation_filter:
					occupation_filter.append(occupation.name)

	return render(request, 'marketplace/search.html', {'results': results,
												'search_form': form,
												'hits': hits,
												'occupation_filter': occupation_filter,
												'interest_filter': interest_filter,
												'query': query})

def profile_has_interest(chosen_interests, profile):
	for interest in profile.interest_set.all():
		if interest.name in chosen_interests:
			return True
	return False

def profile_has_occupation(chosen_occupations, profile):
	for occupation in profile.occupation_set.all():
		if occupation.name in chosen_occupations:
			return True
	return False

def filter(request):
	chosen_occupations = request.GET.getlist('occupation')
	chosen_interests = request.GET.getlist('interest')
	query = request.GET.get('query').encode('ascii')
	form = SearchForm(query=query)

	results = Profile.objects.filter(local=True, city__id=query).order_by('user__first_name')

	occupation_filter = []
	interest_filter = []

	for result in results:
		interests = result.interest_set.all()
		occupations = result.occupation_set.all()

		for interest in interests:
			if interest.name not in interest_filter:
				interest_filter.append(interest.name)

		for occupation in occupations:
			if occupation.name not in occupation_filter:
				occupation_filter.append(occupation.name)

	if len(chosen_occupations) > 0:
		for result in results:
			if not profile_has_occupation(chosen_occupations, result):
				results = results.exclude(user=result.user)

	if len(chosen_interests) > 0:
		for result in results:
			if not profile_has_interest(chosen_interests, result):
				results = results.exclude(user=result.user)

	hits = len(results)

	return render(request, 'marketplace/search.html', {'results': results,
												'search_form': form,
												'hits': hits,
												'occupation_filter': occupation_filter,
												'interest_filter': interest_filter,
												'query': query,
												'chosen_occupations': chosen_occupations,
												'chosen_interests': chosen_interests})
