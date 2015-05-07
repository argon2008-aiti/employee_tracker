# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Safety_Manager'
        db.create_table(u'monitor_safety_manager', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
        ))
        db.send_create_signal(u'monitor', ['Safety_Manager'])

        # Adding model 'Employee'
        db.create_table(u'monitor_employee', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('identification_number', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('location_device', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['monitor.GPS_Device'], null=True)),
        ))
        db.send_create_signal(u'monitor', ['Employee'])

        # Adding model 'Alert'
        db.create_table(u'monitor_alert', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('device', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['monitor.GPS_Device'])),
            ('alert_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('acknowledged', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'monitor', ['Alert'])

        # Adding model 'GPS_Device'
        db.create_table(u'monitor_gps_device', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('identification_number', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('location_LAT', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('location_LON', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal(u'monitor', ['GPS_Device'])


    def backwards(self, orm):
        # Deleting model 'Safety_Manager'
        db.delete_table(u'monitor_safety_manager')

        # Deleting model 'Employee'
        db.delete_table(u'monitor_employee')

        # Deleting model 'Alert'
        db.delete_table(u'monitor_alert')

        # Deleting model 'GPS_Device'
        db.delete_table(u'monitor_gps_device')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'monitor.alert': {
            'Meta': {'object_name': 'Alert'},
            'acknowledged': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'alert_date': ('django.db.models.fields.DateTimeField', [], {}),
            'device': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['monitor.GPS_Device']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'monitor.employee': {
            'Meta': {'object_name': 'Employee'},
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'identification_number': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'location_device': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['monitor.GPS_Device']", 'null': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '15'})
        },
        u'monitor.gps_device': {
            'Meta': {'object_name': 'GPS_Device'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'identification_number': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'location_LAT': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'location_LON': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        u'monitor.safety_manager': {
            'Meta': {'object_name': 'Safety_Manager'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'})
        }
    }

    complete_apps = ['monitor']