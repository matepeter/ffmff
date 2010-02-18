from models import Event, Tag
from forms import EventForm
from django.http import Http404
from django.shortcuts import render_to_response
from django.template import RequestContext

def view_event(request, id):
	try:
		event = Event.objects.get(pk=id)
	except Event.DoesNotExist:
		raise Http404
	
	return render_to_response('events/view_event.html',
	                          { 'event': event },
	                          context_instance=RequestContext(request))

def submit_event(request):
	if request.method == 'POST':
		form = EventForm(request.POST)
		if form.is_valid():
			event = Event()
			event.name = form.cleaned_data['name']
			event.desc = form.cleaned_data['desc']
			event.url = form.cleaned_data['url']
			event.published = False
			event.save()
			return HttpResponseRedirect('/events/submit/success/')
	else:
		form = EventForm()
	
	return render_to_response('events/submit_event.html',
	                          { 'form': form },
	                          context_instance=RequestContext(request))
