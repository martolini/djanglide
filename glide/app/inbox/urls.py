from django.conf.urls import patterns, url

urlpatterns = patterns('glide.app.inbox.views',
	url(r'^$', 'inbox', name='inbox'),
	url(r'^(?P<id>\d+)/$', 'view_conversation', name='view_conversation'),
	url(r'^reply/$', 'reply', name='reply_to_message'),
	url(r'^(?P<id>\d+)/new/$', 'new_message', name='new_message'),
)