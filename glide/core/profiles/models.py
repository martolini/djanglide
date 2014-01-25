from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from glide.core.models import City
from django.core.urlresolvers import reverse
from django.db.models.signals import post_save
from glide.core.countries import COUNTRIES
from glide.core.states import STATES

class Profile(models.Model):
	GENDER_CHOICES = (
		('M', 'Male'),
		('F', 'Female'),
	)

	user = models.ForeignKey(User, unique=True, verbose_name=_('User'))
	gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True, null=True)
	birthday = models.DateField(verbose_name=_('Birthday'), blank=True, null=True)
	about = models.TextField(verbose_name=_('About'), blank=True, null=True)

	local = models.BooleanField(verbose_name=_('Local'), default=False)

	country = models.CharField(max_length=2, choices=COUNTRIES, blank=True, null=True)
	state = models.CharField(max_length=2, choices=STATES, blank=True, null=True)
	city = models.ForeignKey(City, blank=True, null=True)

	photo = models.ImageField(upload_to='photos/profiles/', blank=True, null=True, verbose_name=_('Profile photo'))	
	validated = models.BooleanField(default=False, verbose_name=_('Validated user'))
	facebook = models.CharField(max_length=100, blank=True, null=True, verbose_name=_('Facebook user'))
	twitter = models.CharField(max_length=100, blank=True, null=True, verbose_name=_('Twitter user'))

	def __unicode__(self):
		return self.user.get_full_name()

	def get_absolute_url(self):
		return reverse('view_another_profile', args=[str(self.user.username)])

	def is_local(self):
		return self.local

	def get_country(self):
		return self.country.name

	def has_facebook(self):
		return self.facebook != ''

	def has_twitter(self):
		return self.twitter != ''

	def short(self):
		if len(self.about) < 120:
			return self.about
		about = ''
		for i in range(120):
			about += self.about[i]
		about += '...'
		return about

	def has_occupation(self):
		try:
			return self.occupation_set.all()[0]
		except:
			return ''


class Occupation(models.Model):
	name = models.CharField(max_length=50, verbose_name=_('Occupation'))
	profiles = models.ManyToManyField(Profile)

	def __unicode__(self):
		return self.name