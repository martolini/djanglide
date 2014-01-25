from django.conf.urls import patterns, url

urlpatterns = patterns('glide.app.contact.views',
	url(r'^$', 'contact', name='contact'),
)