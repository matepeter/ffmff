# This program is free software. It comes without any warranty, to
# the extent permitted by applicable law. You can redistribute it
# and/or modify it under the terms of the Do What The Fuck You Want
# To Public License, Version 2, as published by Sam Hocevar. See
# http://sam.zoy.org/wtfpl/COPYING for more details.

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
