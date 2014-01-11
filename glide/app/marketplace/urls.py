from django.conf.urls import patterns, url

urlpatterns = patterns('glide.app.marketplace.views',
	url(r'^$', 'marketplace', name='marketplace'),
	url(r'search', 'search', name='search_marketplace'),
	url(r'filter', 'filter', name='filter_search'),
)
