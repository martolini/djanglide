from django.conf.urls import patterns, url

urlpatterns = patterns('glide.app.interests.views',
     url(r'^add/$', 'add'),
     url(r'^delete/(?P<id>\d+)/', 'delete', name='delete_interest'),
)