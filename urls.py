# This program is free software. It comes without any warranty, to
# the extent permitted by applicable law. You can redistribute it
# and/or modify it under the terms of the Do What The Fuck You Want
# To Public License, Version 2, as published by Sam Hocevar. See
# http://sam.zoy.org/wtfpl/COPYING for more details.

from django.conf.urls.defaults import *
from settings import DEBUG

urlpatterns = patterns('ffmff.events.views',
	(r'^(page/(?P<page>\d+)/)?$', 'home'),
	(r'^events/', include('ffmff.events.urls')),
)

# Home
urlpatterns += patterns('django.views.generic.simple',
	(r'^$', 'direct_to_template', {'template': 'home.html'}),
	(r'^search/', include('haystack.urls')),
	(r'^about/$', 'direct_to_template', {'template': 'about.html'}),
)

if DEBUG:
	# serve static files in debug mode
	from settings import MEDIA_URL, MEDIA_ROOT
	urlpatterns += patterns('django.views.static',
		(r'^%s(?P<path>.*)$' % MEDIA_URL[1:], 'serve', 
		        {'document_root': MEDIA_ROOT, 'show_indexes': True}),
	)

	# admin page
	from django.contrib import admin
	admin.autodiscover()
	urlpatterns += patterns('',
		(r'^admin/(.*)', admin.site.root),
	)
