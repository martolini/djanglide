from django.conf.urls import patterns, url

urlpatterns = patterns('glide.app.mission.views',
	url(r'^$', 'mission', name='mission'),
)