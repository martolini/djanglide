from django.db import models
from django.contrib.auth.models import User
from glide.core.profiles.models import Profile
class Meetup(models.Model):
	seen = models.BooleanField(default=False,)
	target_recipient = models.ForeignKey(Profile,verbose_name="The target recipient",related_name="book_recipients")
	target_sender = models.ForeignKey(Profile,verbose_name="The target sender",related_name='book_targets')
	startTime = models.TimeField()
	date = models.DateField()
	message = models.TextField()

	def __unicode__(self):
		return self.response

	def get_sender(self):
		return self.target_sender.user.get_full_name().title()

class BookRequest(models.Model):
	meetup = models.ForeignKey(Meetup,verbose_name="The meetup object")
	response = models.NullBooleanField(null=True,)
	target_recipient = models.ForeignKey(Profile, verbose_name="The target recipient",related_name='bookreq_recipients')
	def get_meetup(self):
		return self.meetup