# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Employee.location_device'
        db.alter_column(u'monitor_employee', 'location_device_id', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['monitor.GpsDevice'], unique=True, null=True))
        # Adding unique constraint on 'Employee', fields ['location_device']
        db.create_unique(u'monitor_employee', ['location_device_id'])


    def backwards(self, orm):
        # Removing unique constraint on 'Employee', fields ['location_device']
        db.delete_unique(u'monitor_employee', ['location_device_id'])


        # Changing field 'Employee.location_device'
        db.alter_column(u'monitor_employee', 'location_device_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['monitor.GpsDevice'], null=True))

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
            'device': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['monitor.GpsDevice']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'monitor.employee': {
            'Meta': {'object_name': 'Employee'},
            'avatar': ('django.db.models.fields.files.ImageField', [], {'default': "'/static/profile/default.png'", 'max_length': '100', 'blank': 'True'}),
            'department': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'identification_number': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'location_device': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['monitor.GpsDevice']", 'unique': 'True', 'null': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'role': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True'})
        },
        u'monitor.gpsdevice': {
            'Meta': {'object_name': 'GpsDevice'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'identification_number': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'lastest_data': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'auto_now': 'True', 'blank': 'True'}),
            'location': ('djgeojson.fields.PointField', [], {'null': 'True'}),
            'online': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'monitor.safetymanager': {
            'Meta': {'object_name': 'SafetyManager'},
            'employee': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['monitor.Employee']", 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'})
        }
    }

    complete_apps = ['monitor']