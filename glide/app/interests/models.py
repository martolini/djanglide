from django.db import models
from glide.core.profiles.models import Profile
from django.utils.translation import ugettext_lazy as _

class Interest(models.Model):
	name = models.CharField(max_length=50, verbose_name=_('Name'))
	profiles = models.ManyToManyField(Profile, null=True)

	def __unicode__(self):
		return self.name