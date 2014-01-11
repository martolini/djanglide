from django.conf.urls import patterns, url

urlpatterns = patterns('glide.app.testimonial.views',
	url(r'^add/(?P<username>\w+)/$', 'add', name='add_testimonial'),
)