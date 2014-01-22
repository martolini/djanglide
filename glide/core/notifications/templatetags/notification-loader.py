from django.template.base import Library
from glide.app.interests.forms import InterestForm
from glide.core.notifications.models import Notification

register = Library()

@register.inclusion_tag('templatetags/notifications.html', takes_context=True)
def load_notifications(context, profile):
	notifications = Notification.objects.filter(target_recipient=profile,seen=False)
	return {'notifications':notifications}