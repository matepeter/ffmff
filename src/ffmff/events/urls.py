from django.conf.urls.defaults import *
from models import Event, Tag
from django.views.generic.simple import direct_to_template

from django.contrib import admin
admin.site.register(Event)
admin.site.register(Tag)

urlpatterns = patterns('ffmff.events.views',
	(r'^submit/$', 'submit_event'),
	(r'^submit/success/$', direct_to_template, {'template': 'events/submit_success.html'}),
	(r'^(?P<id>\d)/$', 'view_event'),
)
