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
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from ffmff.decorators import raise_404
from datetime import datetime, timedelta
from string import replace

def event_pagination(events, page):
	# 5 events per page, 10 would be too much
	paginator = Paginator(events, 5)

	# Make sure page request is an int. If not, deliver first page.
	try:
		page = int(page)
	except (ValueError, TypeError):
		page = 1

	# If page request (9999) is out of range, deliver last page of results.
	try:
		events = paginator.page(page)
	except (EmptyPage, InvalidPage):
		events = paginator.page(paginator.num_pages)

	return events

def home(request, page):
	events = Event.objects.filter(published=True, date_end__gte=datetime.now())
	events = events.order_by('date_start')
	events = event_pagination(events, page)

	return render_to_response('home.html',
		{'events': events,}, context_instance=RequestContext(request))

def past_events(request, page):
	events = Event.objects.filter(published=True, date_end__lt=datetime.now())
	events = events.order_by('-date_start')
	events = event_pagination(events, page)

	return render_to_response('events/past.html',
		{'events': events,}, context_instance=RequestContext(request))
 

@raise_404
def view_event(request, id):
	event = Event.objects.get(pk=id)

	if not event.published:
		raise Http404

	# We need this for Google Calendar export, otherwise the event will end one day early
	enddate_plusone = event.date_end + timedelta(days=1)

	return render_to_response('events/view_event.html',
			{'event': event, 'enddate_plusone': enddate_plusone}, context_instance=RequestContext(request))

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
			event.submit_ip = request.META['REMOTE_ADDR']
			event.save()
			return HttpResponseRedirect('/events/submit/success/')
	else:
		form = EventForm()

	return render_to_response('events/submit_event.html',
		{'form': form}, context_instance=RequestContext(request))

@raise_404
def export_ical(request, id):
	event = Event.objects.get(pk=id)

	if not event.published:
		raise Http404

	enddate_plusone = event.date_end + timedelta(days=1)
	ical_desc = replace(event.desc, '\n', '\\n')
	ical_desc = replace(ical_desc, '\r', '')

	t = get_template('events/export_ical.ics')

	render = t.render(Context(
		{
			'event': event,
			'enddate_plusone': enddate_plusone,
			'ical_desc': ical_desc,
		}
	))

	response = HttpResponse(render, mimetype='text/calendar')
	response['Content-Disposition'] = 'attachment; filename=ffmff_event_%s.ics' % event.pk

	return response
