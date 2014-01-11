from django.conf.urls import patterns, url

urlpatterns = patterns('glide.core.profiles.views',
	url(r'^$', 'account', name='account'),
	url(r'^logout/$', 'logout', name='logout'),
	url(r'^view/(?P<username>\w+)/$', 'view_profile', name='view_another_profile'),
	url(r'^edit_profile/$', 'edit_profile', name='edit_profile'),
	url(r'^auth/$', 'auth_view', name='auth_view'),
	url(r'^add_occupation/$', 'add_occupation', name='add_occupation'),
	url(r'^add_photo/$', 'add_photo', name='add_photo'),
	url(r'^be_local/$', 'be_local', name='be_local'),
)

