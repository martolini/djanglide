from django.conf.urls import patterns, url

urlpatterns = patterns('glide.app.booking.views',
	url(r'^book/$', 'book_profile', name='book_profile'),
)