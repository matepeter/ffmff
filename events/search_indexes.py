# This program is free software. It comes without any warranty, to
# the extent permitted by applicable law. You can redistribute it
# and/or modify it under the terms of the Do What The Fuck You Want
# To Public License, Version 2, as published by Sam Hocevar. See
# http://sam.zoy.org/wtfpl/COPYING for more details.

from datetime import datetime
from haystack import indexes
from haystack import site
from models import Event

# using RealTimeSearchIndex atm: performance?
class EventIndex(indexes.RealTimeSearchIndex):
	text = indexes.CharField(document=True, use_template=True)
	date_start = indexes.DateField(model_attr='date_start')
	date_end = indexes.DateField(model_attr='date_end')

	def get_queryset(self):
		"""Used when the entire index for model is updated."""
		return Event.objects.exclude(date_end__lte=datetime.now()).exclude(published__exact=False)

site.register(Event, EventIndex)
