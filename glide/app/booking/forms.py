from django.forms.models import ModelForm
from django.utils.translation import ugettext_lazy as _
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from glide.core.profiles.models import Profile, Occupation
from glide.core.models import City

class BookForm(ModelForm):
	message = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Send a message to let them know about your visit!'}))
	date = forms.DateField()
	class Meta:
		model = Booked
		exclude = ('target_sender','target_recipient',)