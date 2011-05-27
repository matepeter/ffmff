from django import template
from datetime import datetime

register = template.Library()

@register.inclusion_tag('events/mini_calendar.html')
def mini_calendar(date_begin, date_end):
	past = date_end < datetime.now().date()
	return {
		'date_begin': date_begin,
		'date_end': date_end,
		'past': past
	}
