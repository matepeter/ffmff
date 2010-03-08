
from south.db import db
from django.db import models
from ffmff.events.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding model 'Event'
        db.create_table('events_event', (
            ('id', orm['events.Event:id']),
            ('name', orm['events.Event:name']),
            ('desc', orm['events.Event:desc']),
            ('url', orm['events.Event:url']),
            ('date_start', orm['events.Event:date_start']),
            ('date_end', orm['events.Event:date_end']),
            ('published', orm['events.Event:published']),
            ('submit_ip', orm['events.Event:submit_ip']),
        ))
        db.send_create_signal('events', ['Event'])
        
        # Adding model 'Tag'
        db.create_table('events_tag', (
            ('id', orm['events.Tag:id']),
            ('tag', orm['events.Tag:tag']),
        ))
        db.send_create_signal('events', ['Tag'])
        
        # Adding ManyToManyField 'Event.tags'
        db.create_table('events_event_tags', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('event', models.ForeignKey(orm.Event, null=False)),
            ('tag', models.ForeignKey(orm.Tag, null=False))
        ))
        
    
    
    def backwards(self, orm):
        
        # Deleting model 'Event'
        db.delete_table('events_event')
        
        # Deleting model 'Tag'
        db.delete_table('events_tag')
        
        # Dropping ManyToManyField 'Event.tags'
        db.delete_table('events_event_tags')
        
    
    
    models = {
        'events.event': {
            'date_end': ('django.db.models.fields.DateField', [], {}),
            'date_start': ('django.db.models.fields.DateField', [], {}),
            'desc': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'submit_ip': ('django.db.models.fields.IPAddressField', [], {'max_length': '15'}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['events.Tag']", 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        'events.tag': {
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tag': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }
    
    complete_apps = ['events']
