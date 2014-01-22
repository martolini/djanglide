from django.shortcuts import render
from glide.core.notifications.models import Notification

def mark_as_read(request):
	results = {'success':False}
	if request.method == u'GET':
		GET = request.GET
		if GET.has_key(u'pk'):
			pk = int(GET[u'pk'])
			notifications = Notification.objects.filter(target_recipient=pk,seen=False)
			for notification in notifications:
				notification.mark_as_seen()
				notification.save()
				print "Hello"
			results = {'success':True}
	json = simplejson.dumps(results)
	return HttpResponse(json, mimetype='application/json')