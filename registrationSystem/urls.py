from django.conf.urls import patterns, include, url
from dajaxice.core import dajaxice_autodiscover, dajaxice_config
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
import settings

admin.autodiscover()
dajaxice_autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'home.views.home_view'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(dajaxice_config.dajaxice_url, include('dajaxice.urls')),
)

if settings.DEBUG:
    urlpatterns += patterns('',
			 url(r'^media/(?P<path>.*)$',
				 'django.views.static.serve',
				 {'document_root': settings.MEDIA_ROOT}),
				 )

