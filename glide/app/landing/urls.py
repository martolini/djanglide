from django.conf.urls import patterns, url

urlpatterns = patterns('glide.app.landing.views',
	url(r'^$', 'frontpage', name='frontpage'),
)
