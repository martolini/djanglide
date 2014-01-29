from django.conf.urls import patterns, url

urlpatterns = patterns('glide.app.booking.views',
	url(r'^(?P<id>\d+)/book/$', 'book_profile', name='book_profile'),
	url(r'^requests$', 'book_requests', name='book_requests'),
)