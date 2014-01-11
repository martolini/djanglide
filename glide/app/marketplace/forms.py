from django.forms.forms import Form
from django import forms
from glide.core.models import City

class SearchForm(Form):
	query = forms.ChoiceField()

	def __init__(self, *args, **kwargs):
		try:
			default = kwargs.pop('query', None)
		except:
			default = False
		super(SearchForm, self).__init__(*args, **kwargs)
		cities = City.objects.filter(has_local=True).order_by('name')
		self.fields['query'].choices = [(city.pk, city) for city in cities]
		if not default:
			self.fields['query'].choices.insert(0, ('',"I'm looking for a guide in..." ) )
		else:
			self.fields['query'].initial = default

