from django.db import models
from django.contrib.auth.models import User
class Notification(models.Model):
	actionType = models.CharField(max_length=1)
	target_recipient = models.ForeignKey(User,verbose_name="The target recipient",related_name='notification_recipients')
	target_sender = models.ForeignKey(User,verbose_name="The target sender",related_name='notification_targets',null=True)
	seen = models.BooleanField(default=False,verbose_name="Seen or not")

	def __unicode__(self):
		return self.target_recipient

	def mark_as_seen(self):
		self.seen = True

	def get_noti_string(self):
		if(self.actionType=="message"):
			return 	self.target_sender.get_full_name() + " sent you a new message!"
		elif(self.actionType=="review"):
			return self.target_sender.get_full_name() + " reviewed you!"
		elif(self.actionType=="local"):
			return "You have just become a local!"
		elif(self.actionType=="non-local"):
			return "You have just resigned from being a local!"
		elif(self.actionType=="book"):
			return "You have just been sent a book request by " + self.target_sender.get_full_name().title() + "!"
		else:
			return "Nothing"

	def get_url_string(self):
		if(self.actionType=="message"):
			return 	"/inbox/"
		elif(self.actionType=="review"):
			return 	"/profile/"
		elif(self.actionType=="local"):
			return 	"/profile/"
		elif(self.actionType=="non-local"):
			return 	"/profile/"
		elif(self.actionType=="book"):
			return 	"/book/"
		else:
			return "Nothing"
