from django.db import models
from glide.core.countries import COUNTRIES
from glide.core.states import STATES

class City(models.Model):
	name = models.CharField(max_length=50, unique=True)
	country = models.CharField(max_length=2, choices=COUNTRIES, null=True)
	state = models.CharField(max_length=2, choices=STATES, null=True)
	has_local = models.BooleanField(default=False)

	def __unicode__(self):
		return self.name

	class Meta:
		verbose_name_plural = "Cities"