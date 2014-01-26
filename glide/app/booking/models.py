from django.db import models
from django.contrib.auth.models import User

class Booked(models.Model):
	DateTime = models.DateTimeField()
	target_recipient = models.ForeignKey(User,verbose_name="The target recipient",related_name="book_recipients")
	target_sender = models.ForeignKey(User,verbose_name="The target sender",related_name='book_targets',null=True)
	message = models.TextField()

	def __unicode__(self):
		return self.date

class Meetup(models.Model):
	seen = models.BooleanField(default=False,)
	response = models.BooleanField(default=False,)
	info = models.ForeignKey(Booked,verbose_name="The corresponding booked object")

	def __unicode__(self):
		return self.response