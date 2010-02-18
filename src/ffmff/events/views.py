from models import Event, Tag
from django.http import Http404
from django.shortcuts import render_to_response
from django.template import RequestContext

def view_event(request, id):
	try:
		event = Event.objects.get(pk=id)
	except Event.DoesNotExist:
		raise Http404
	
	return render_to_response('events/view_event.html',
	                          {
	                              'event': event,
	                          },
	                          context_instance=RequestContext(request))
