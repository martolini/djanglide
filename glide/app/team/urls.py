from django.conf.urls import patterns, url

urlpatterns = patterns('glide.app.team.views',
	url(r'^$', 'team', name='team'),
)