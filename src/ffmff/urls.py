from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	(r'^events/', include('ffmff.events.urls')),
	(r'^admin/(.*)', admin.site.root),
)
