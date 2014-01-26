from django.forms.models import ModelForm
from django.utils.translation import ugettext_lazy as _
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from glide.core.profiles.models import Profile, Occupation
from glide.core.models import City
class LandingRegistrationForm(UserCreationForm):

	first_name = forms.CharField()
	last_name = forms.CharField()
	email = forms.EmailField()

	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')


	def save(self, commit=True):
		user = super(LandingRegistrationForm, self).save(commit=False)
		user.first_name = self.cleaned_data['first_name']
		user.last_name = self.cleaned_data['last_name']
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
			Profile(user=user).save()
		return user

	def clean(self):
		super(LandingRegistrationForm, self).clean()
		#if self.cleaned_data.get('username'):
		#	valid = re.match('^[\w-]+$', self.cleaned_data.get('username')) is not None
		#	if not valid:
		#		self._errors['username'] = "Only alphanumeric characters in username"
		return self.cleaned_data



class OccupationForm(ModelForm):
	name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'New occupation'}))

	class Meta:
		model = Occupation
		exclude = ('profiles',)

class PhotoForm(ModelForm):
	class Meta:
		model = Profile
		exclude = ('user', 'gender', 'birthday', 'about', 'local', 'country', 'state',
			'city', 'validated', 'facebook', 'twitter')

class ProfileForm(ModelForm):
	new_city = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'New city'}), required=False)
	new_email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'New email'}), required=False)
	new_first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'New first name'}), required=False)
	new_last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'New last name'}), required=False)
	new_occupation = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'New occupation'}), required=False)

	class Meta:
		model = Profile
		exclude = ('user', 'local', 'validated', 'facebook', 'twitter', 'city')

	def __init__(self, *args, **kwargs):
		profile = kwargs.pop('instance')
		super(ProfileForm, self).__init__(*args, **kwargs)
		self.fields['new_city'].initial = profile.city
		self.fields['new_email'].initial = profile.user.email
		self.fields['new_first_name'].initial = profile.user.first_name
		self.fields['new_last_name'].initial = profile.user.last_name
		self.fields['gender'].initial = profile.gender
		self.fields['birthday'].initial = profile.birthday
		self.fields['birthday'].widget.attrs['placeholder'] = 'YYYY-MM-DD'
		self.fields['about'].initial = profile.about
		self.fields['country'].initial = profile.country
		self.fields['state'].initial = profile.state
		self.fields['photo'].initial = profile.photo
		self.fields['photo'].widget = forms.FileInput()
		try:
			self.fields['new_occupation'].initial = profile.occupation_set.all()[0]
		except:
			pass
