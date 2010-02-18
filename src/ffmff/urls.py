from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	(r'^events/', include('ffmff.events.urls')),
	(r'^admin/(.*)', admin.site.root),
)

# Home
urlpatterns += patterns('django.views.generic.simple',
	(r'^$', 'direct_to_template', {'template': 'home.html'}),
)
