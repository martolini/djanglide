from django.template.base import Library

register = Library()

@register.filter
def occupation_is_checked(occupation, chosen_occupations):
	return occupation in chosen_occupations

@register.filter
def interest_is_checked(interest, chosen_interests):
	return interest in chosen_interests
