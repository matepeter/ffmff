from django.conf.urls.defaults import *
from settings import DEBUG

urlpatterns = patterns('',
	(r'^events/', include('ffmff.events.urls')),
)

# Home
urlpatterns += patterns('django.views.generic.simple',
	(r'^$', 'direct_to_template', {'template': 'home.html'}),
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
