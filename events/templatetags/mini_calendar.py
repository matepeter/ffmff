from django import template
from datetime import datetime

register = template.Library()

@register.inclusion_tag('events/mini_calendar.html')
def mini_calendar(date):
	past = date < datetime.now().date()
	return {'date': date, 'past': past}
