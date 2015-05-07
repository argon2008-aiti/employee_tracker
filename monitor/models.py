from django.db import models
from django.contrib.auth.models import User


class GPS_Device(models.Model):
    identification_number = models.CharField(max_length=20)
    location_LAT          = models.CharField(max_length=20)
    location_LON          = models.CharField(max_length=20)

    def __unicode__(self):
        return self.identification_number

class Employee(models.Model):
    identification_number = models.CharField(max_length=20)
    first_name            = models.CharField(max_length=20)
    last_name             = models.CharField(max_length=20)
    phone                 = models.CharField(max_length=15)
    location_device       = models.ForeignKey(GPS_Device, null=True)
     
    def __unicode__(self):
        return self.first_name + " " + self.last_name

class Safety_Manager(models.Model):
    user = models.OneToOneField(User)

    def __unicode__(self):
        return self.user.username

class Alert(models.Model):
    device         = models.ForeignKey(GPS_Device)
    alert_date     = models.DateTimeField()
    acknowledged   = models.BooleanField(default=False)

    def __unicode__(self):
        return self.device.identification_number

