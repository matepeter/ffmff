# This program is free software. It comes without any warranty, to
# the extent permitted by applicable law. You can redistribute it
# and/or modify it under the terms of the Do What The Fuck You Want
# To Public License, Version 2, as published by Sam Hocevar. See
# http://sam.zoy.org/wtfpl/COPYING for more details.

from django import forms

class EventForm(forms.Form):
	name = forms.CharField(max_length=50)
	desc = forms.CharField(max_length=5000, widget=forms.Textarea)
	url  = forms.URLField(max_length=100)
	date_start = forms.DateField()
	date_end   = forms.DateField()
