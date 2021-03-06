# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Safety_Manager.employee'
        db.add_column(u'monitor_safety_manager', 'employee',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['monitor.Employee'], null=True),
                      keep_default=False)

        # Adding field 'Employee.role'
        db.add_column(u'monitor_employee', 'role',
                      self.gf('django.db.models.fields.CharField')(max_length=25, null=True),
                      keep_default=False)

        # Adding field 'Employee.department'
        db.add_column(u'monitor_employee', 'department',
                      self.gf('django.db.models.fields.IntegerField')(null=True),
                      keep_default=False)

        # Deleting field 'GPS_Device.location_LON'
        db.delete_column(u'monitor_gps_device', 'location_LON')

        # Deleting field 'GPS_Device.location_LAT'
        db.delete_column(u'monitor_gps_device', 'location_LAT')

        # Adding field 'GPS_Device.location'
        db.add_column(u'monitor_gps_device', 'location',
                      self.gf('djgeojson.fields.PointField')(null=True),
                      keep_default=False)

        # Adding field 'GPS_Device.status'
        db.add_column(u'monitor_gps_device', 'status',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Safety_Manager.employee'
        db.delete_column(u'monitor_safety_manager', 'employee_id')

        # Deleting field 'Employee.role'
        db.delete_column(u'monitor_employee', 'role')

        # Deleting field 'Employee.department'
        db.delete_column(u'monitor_employee', 'department')

        # Adding field 'GPS_Device.location_LON'
        db.add_column(u'monitor_gps_device', 'location_LON',
                      self.gf('django.db.models.fields.CharField')(default=2, max_length=20),
                      keep_default=False)

        # Adding field 'GPS_Device.location_LAT'
        db.add_column(u'monitor_gps_device', 'location_LAT',
                      self.gf('django.db.models.fields.CharField')(default=1, max_length=20),
                      keep_default=False)

        # Deleting field 'GPS_Device.location'
        db.delete_column(u'monitor_gps_device', 'location')

        # Deleting field 'GPS_Device.status'
        db.delete_column(u'monitor_gps_device', 'status')


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
            'department': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'identification_number': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'location_device': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['monitor.GPS_Device']", 'null': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'role': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True'})
        },
        u'monitor.gps_device': {
            'Meta': {'object_name': 'GPS_Device'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'identification_number': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'location': ('djgeojson.fields.PointField', [], {'null': 'True'}),
            'status': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'monitor.safety_manager': {
            'Meta': {'object_name': 'Safety_Manager'},
            'employee': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['monitor.Employee']", 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'})
        }
    }

    complete_apps = ['monitor']