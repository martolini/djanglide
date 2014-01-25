from django.forms.models import ModelForm
from glide.app.inbox.models import Message, Conversation
from django.forms.widgets import HiddenInput

class ReplyMessageForm(ModelForm):
	class Meta:
		model = Message
		exclude = ('author', 'read')
        widgets = {
                'conversation': HiddenInput(),
            }

class NewMessageForm(ModelForm):
	class Meta:
		model = Message
		exclude = ('author', 'read', 'conversation')