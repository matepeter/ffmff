from django import template
register = template.Library()

@register.inclusion_tag('events/event.html')
def event(event):
	return {'e':event}

@register.inclusion_tag('events/event.html')
def event_nolink(event):
	return {'e':event, 'nolink':True}

