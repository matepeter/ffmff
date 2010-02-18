from django.db import models

class Event(models.Model):
	name = models.CharField(max_length=50)
	desc = models.TextField()
	url  = models.URLField()
	# img  = 
	date_start = models.DateField()
	date_end   = models.DateField()
	tags = models.ManyToManyField('Tag', blank=True)
	published = models.BooleanField()
	
	def __unicode__(self):
		return self.name
	
	def get_absolute_url(self):
		return '/events/%i/' % self.pk

class Tag(models.Model):
	tag  = models.CharField(max_length=30)
	
	def __unicode__(self):
		return self.tag
