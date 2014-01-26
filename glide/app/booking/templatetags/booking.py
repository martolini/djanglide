from django.template.base import Library
from glide.app.inbox.forms import ReplyMessageForm
from glide.app.inbox.models import Message, Conversation
from django.db.models import Q

register = Library()
