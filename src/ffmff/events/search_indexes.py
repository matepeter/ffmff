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
		return Event.objects.filter(date_end__gte=datetime.now()).filter(published__exact=True)

site.register(Event, EventIndex)
