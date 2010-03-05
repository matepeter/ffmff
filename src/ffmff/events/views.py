# This program is free software. It comes without any warranty, to
# the extent permitted by applicable law. You can redistribute it
# and/or modify it under the terms of the Do What The Fuck You Want
# To Public License, Version 2, as published by Sam Hocevar. See
# http://sam.zoy.org/wtfpl/COPYING for more details.

from models import Event, Tag
from forms import EventForm
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext, Context
from django.template.loader import get_template
from ffmff.decorators import raise_404
from datetime import timedelta
from string import replace

@raise_404
def view_event(request, id):
	event = Event.objects.get(pk=id)

	if not event.published:
		raise Http404

	return render_to_response('events/view_event.html',
	                          { 'event': event },
	                          context_instance=RequestContext(request))

def submit_event(request):
	if request.method == 'POST':
		if request.POST.has_key('abort'):
			return HttpResponseRedirect('/')
		form = EventForm(request.POST)
		if form.is_valid():
			event = Event()
			event.name = form.cleaned_data['name']
			event.desc = form.cleaned_data['desc']
			event.url = form.cleaned_data['url']
			event.date_start = form.cleaned_data['date_start']
			event.date_end   = form.cleaned_data['date_end']
			event.published = False
			event.save()
			return HttpResponseRedirect('/events/submit/success/')
	else:
		form = EventForm()

	return render_to_response('events/submit_event.html',
	                          { 'form': form },
	                          context_instance=RequestContext(request))

@raise_404
def export_ical(request, id):
	event = Event.objects.get(pk=id)

	if not event.published:
		raise Http404

	ical_enddate = event.date_end + timedelta(days=1)
	ical_desc = replace(event.desc, '\n', '\\n')
	ical_desc = replace(ical_desc, '\r', '')

	t = get_template('events/export_ical.ics')
	render = t.render(Context({ 'event': event, 
	                            'ical_enddate': ical_enddate,
	                            'ical_desc': ical_desc, }))

	response = HttpResponse(render, mimetype='text/calendar')
	response['Content-Disposition'] = 'attachment; filename=ffmff_event_%s.ics' % event.pk

	return response
