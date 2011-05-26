# This program is free software. It comes without any warranty, to
# the extent permitted by applicable law. You can redistribute it
# and/or modify it under the terms of the Do What The Fuck You Want
# To Public License, Version 2, as published by Sam Hocevar. See
# http://sam.zoy.org/wtfpl/COPYING for more details.

from django.db import models

class Event(models.Model):
	name = models.CharField(max_length=50)
	desc = models.TextField()
	url  = models.URLField()
	img  = models.ImageField(null=True, upload_to='events/', blank=True) 
	date_start = models.DateField()
	date_end   = models.DateField()
	tags = models.ManyToManyField('Tag', blank=True)
	published = models.BooleanField()
	submit_ip = models.IPAddressField(blank=True)
	location = models.TextField(blank=True)
	geoloc = models.TextField(blank=True)

	def __unicode__(self):
		return self.name

	def get_absolute_url(self):
		return '/events/%i/' % self.pk

class Tag(models.Model):
	tag  = models.CharField(max_length=30)

	def __unicode__(self):
		return self.tag
