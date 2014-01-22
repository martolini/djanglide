from django.conf.urls import patterns, url

urlpatterns = patterns('glide.core.notifications.views',
	url(r'^read/$', 'mark_as_read'),
)

