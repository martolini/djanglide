from django.template.base import Library
from glide.app.interests.forms import InterestForm
from glide.core.notifications.models import Notification

register = Library()

@register.simple_tag
def mark_as_read():
	unread_notifications = Notification.objects.filter(seen=False)
	unread_notifications.mark_as_seen()