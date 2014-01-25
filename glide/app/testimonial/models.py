from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from glide.core.profiles.models import Profile

class Testimonial(models.Model):
	user = models.ForeignKey(User, blank=True, null=True, verbose_name=_('User'), related_name='+')
	author = models.ForeignKey(User, blank=True, null=True, verbose_name=_('Written by'))
	date = models.DateTimeField(auto_now_add=True, verbose_name=_('Date'))
	content = models.TextField(verbose_name=_('Content'))
	rating = models.IntegerField(null=True, verbose_name=_('Rating'))

	def __unicode__(self):
		return unicode(self.user)

	def short(self):
		if len(self.content) < 160:
			return self.content
		snippet = ""
		for i in range(160):
			snippet += self.content[i]
		snippet += "..."
		return snippet

	def get_author_photo(self):
		profile = Profile.objects.get(user=self.author)
		return profile.photo
