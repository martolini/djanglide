from django.forms.models import ModelForm
from django.utils.translation import ugettext_lazy as _
from django import forms
from glide.app.booking.models import Meetup
class BookForm(ModelForm):
	date = forms.DateField(widget=forms.TextInput(attrs=
                                {
                                    'id':'datepicker'
                                }),input_formats=['%Y-%m-%d',])
	startTime = forms.TimeField(widget=forms.TextInput(attrs=
                                {
                                    'id':'timepicker'
                                }),label="Start Time",input_formats=['%I:%M%p',])
	message = forms.CharField(label="Message",widget=forms.Textarea)
	class Meta:
		model = Meetup
		exclude = ('target_sender','target_recipient','seen',)
