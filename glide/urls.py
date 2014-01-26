from django.conf.urls import patterns, include, url
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^', include('glide.app.landing.urls')),
    url(r'^profile/', include('glide.core.profiles.urls')),
    url(r'^testimonial/', include('glide.app.testimonial.urls')),
    url(r'^inbox/', include('glide.app.inbox.urls')),
    url(r'^marketplace/', include('glide.app.marketplace.urls')),
    url(r'^interests/', include('glide.app.interests.urls')),
    url(r'^about/', include('glide.app.mission.urls')),
    url(r'^team/', include('glide.app.team.urls')),
    url(r'^contact/', include('glide.app.contact.urls')),
    url(r'^notifications/', include('glide.core.notifications.urls')),
    url(r'^book/', include('glide.app.booking.urls')),
)

urlpatterns += patterns('',
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve',
         {'document_root': settings.MEDIA_ROOT}),
        (r'^uploads/(?P<path>.*)$', 'django.views.static.serve',
         {'document_root': settings.MEDIA_ROOT}),
    )
