from django.db import models
from django.contrib.auth.models import User

class Meetup(models.Model):
	seen = models.BooleanField(default=False,)
	target_recipient = models.ForeignKey(User,verbose_name="The target recipient",related_name="book_recipients")
	target_sender = models.ForeignKey(User,verbose_name="The target sender",related_name='book_targets',null=True)
	startTime = models.TimeField()
	date = models.DateField()
	message = models.TextField()

	def __unicode__(self):
		return self.response

class BookRequest(models.Model):
	meetup = models.ForeignKey(Meetup,verbose_name="The meetup object")
	response = models.BooleanField(default=False,)
	def __unicode__(self):
		return self.meetup