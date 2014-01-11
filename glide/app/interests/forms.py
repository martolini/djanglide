from django.forms.models import ModelForm
from django import forms
from glide.app.interests.models import Interest

class InterestForm(ModelForm):
	name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'New interest'}))
	class Meta:
		model = Interest
		exclude = ('profiles',)