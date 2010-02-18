from django.conf.urls.defaults import *
from models import Event, Tag

from django.contrib import admin
admin.site.register(Event)
admin.site.register(Tag)

urlpatterns = patterns('ffmff.events.views',
	(r'^(?P<id>\d)/$', 'view_event'),
)
