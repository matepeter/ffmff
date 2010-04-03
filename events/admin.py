# This program is free software. It comes without any warranty, to
# the extent permitted by applicable law. You can redistribute it
# and/or modify it under the terms of the Do What The Fuck You Want
# To Public License, Version 2, as published by Sam Hocevar. See
# http://sam.zoy.org/wtfpl/COPYING for more details.

from django.contrib import admin
from models import Event, Tag

class EventAdmin(admin.ModelAdmin):
	list_display = ('pk', 'name', 'date_start', 'date_end', 'published')
	list_filter = ('published', 'date_start', 'date_end', 'tags')
	search_fields = ['name']

admin.site.register(Event, EventAdmin)
admin.site.register(Tag)