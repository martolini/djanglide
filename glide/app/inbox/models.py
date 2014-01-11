from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from glide.core.profiles.models import Profile
from django.core.urlresolvers import reverse

class Conversation(models.Model):
	receiver = models.ForeignKey(User, verbose_name=_('Receiver'), related_name='+')
	sender = models.ForeignKey(User, verbose_name=_('Sender'), related_name='+')
	last_message = models.DateTimeField(auto_now=True, null=True)

	def __unicode__(self):
		return "%s's conversation with %s" %(self.receiver, self.sender)

	def receiver_profile(self):
		return Profile.objects.get(user=self.receiver)

	def sender_profile(self):
		return Profile.objects.get(user=self.sender)

	def get_last_message(self):
		messages = Message.objects.filter(conversation=self).order_by('-date')
		try:
			return messages[0]
		except:
			return None

	def get_absolute_url(self):
		return reverse('glide.app.inbox.views.view_conversation', args=[self.pk])

class Message(models.Model):
	conversation = models.ForeignKey(Conversation, null=True, verbose_name=_('Conversation'))
	author = models.ForeignKey(User, null=True, verbose_name=_('Author'), related_name='+')
	content = models.TextField(verbose_name=_('Message'))
	date = models.DateTimeField(auto_now_add=True)
	read = models.BooleanField(default=False, verbose_name=_('Read'))

	def __unicode__(self):
		if len(self.content) < 30:
			return self.content
		snippet = ''
		for i in range(30):
			snippet += self.content[i]
		snippet += '...'
		return snippet

	def author_profile(self):
		return Profile.objects.get(user=self.author)
