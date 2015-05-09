from django.db import models
from django.contrib.auth.models import User
from djgeojson.fields import PointField


DEPARTMENTS = [
       (1, "January"), 
       (2, "February"), 
       (3, "March"), 
       (4, "April"),
       (5, "May"), 
       (6, "June"), 
       (7, "July"), 
       (8, "August"), 
       (9, "September"), 
       (10, "October"), 
       (11, "November"), 
       (12, "December") 
        ]

class GPS_Device(models.Model):
    identification_number = models.CharField(max_length=20)
    location              = PointField(null=True)
    status                = models.BooleanField(default=False)

    def __unicode__(self):
        return self.identification_number


class Employee(models.Model):
    identification_number = models.CharField(max_length=20)
    first_name            = models.CharField(max_length=20)
    last_name             = models.CharField(max_length=20)
    role                  = models.CharField(max_length=25, null=True)
    department		  = models.IntegerField(choices=DEPARTMENTS, null=True)
    phone                 = models.CharField(max_length=15)
    location_device       = models.ForeignKey(GPS_Device, null=True)
     
    def __unicode__(self):
        return self.first_name + " " + self.last_name


class Safety_Manager(models.Model):
    user     = models.OneToOneField(User)
    employee = models.ForeignKey(Employee, null=True)

    def __unicode__(self):
        return self.user.username


class Alert(models.Model):
    device         = models.ForeignKey(GPS_Device)
    alert_date     = models.DateTimeField()
    acknowledged   = models.BooleanField(default=False)

    def __unicode__(self):
        return self.device.identification_number


