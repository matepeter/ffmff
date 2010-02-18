from django import forms

class EventForm(forms.Form):
	name = forms.CharField(max_length=50)
	desc = forms.CharField(max_length=5000, widget=forms.Textarea)
	url  = forms.URLField(max_length=100)
	date_start = forms.DateField()
	date_end   = forms.DateField()
