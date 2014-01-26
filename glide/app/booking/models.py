from django.db import models

class Booked(models.Model):
	date = models.DateField()
	target_recipient = models.ForeignKey(User,verbose_name="The target recipient",related_name="book_recipients")
	target_sender = models.ForeignKey(User,verbose_name="The target sender",related_name='book_targets',null=True)
	message = models.TextField()

	def __unicode__(self):
		return self.date