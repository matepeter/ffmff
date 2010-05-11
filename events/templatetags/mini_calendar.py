from django import template
register = template.Library()

@register.inclusion_tag('mini_calendar.html')
def mini_calendar(date):
	return {'date':date}
