from django.forms.models import ModelForm
from django.utils.translation import ugettext_lazy as _
from django import forms
from django.contrib.auth.models import User
from glide.app.booking.models import Booked
from glide.app.booking.fields import JqSplitDateTimeField
from glide.app.booking.widgets import JqSplitDateTimeWidget
class BookForm(ModelForm):
	message = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Send a message to let them know about your visit!'}))

	class Meta:
		model = Booked
		exclude = ('target_sender','target_recipient',)