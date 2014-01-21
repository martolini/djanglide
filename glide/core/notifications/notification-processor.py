from glide.core.notifications.models import Notification

def notifications(request):
	return {'notifications': Notification.objects.filter(seen=False)}