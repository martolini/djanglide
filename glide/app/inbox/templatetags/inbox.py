from django.template.base import Library
from glide.app.inbox.forms import ReplyMessageForm
from glide.app.inbox.models import Message, Conversation
from django.db.models import Q

register = Library()

@register.inclusion_tag('inbox/templatetags/form.html')
def load_reply_form(conversation):
	form = ReplyMessageForm(instance=Message(conversation=conversation))
	return {'form':form}

@register.simple_tag
def count_all_unread_messages(user):
	amount = 0
	conversations = Conversation.objects.filter(Q(receiver=user) | Q(sender=user))

	for conversation in conversations:
		amount += Message.objects.filter(conversation=conversation).exclude(read=True).exclude(author=user).count()

	if amount == 0:
		return ''
	else:
		return '(%s)' %(amount)

@register.simple_tag
def count_unread_messages(conversation, user):
	amount = 0
	amount += Message.objects.filter(conversation=conversation).exclude(read=True).exclude(author=user).count()
	if amount == 0:
		return ''
	else:
		return '(%s)' %(amount)