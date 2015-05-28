from django.db import models
from django.contrib.auth.models import User
from djgeojson.fields import PointField
import datetime


DEPARTMENTS = [
       (1, "ADMINISTRATION"), 
       (2, "CARBON"), 
       (3, "CAST HOUSE"), 
       (4, "CELL LINES"),
       (5, "DOCKS, ENGINEERING AND MAINTENANCE"), 
       (6, "FINANCE AND COMMERCE"), 
       (7, "TECHNICAL"), 
        ]


class GpsDevice(models.Model):
    identification_number = models.CharField(max_length=20)
    location              = PointField(null=True)
    lastest_data          = models.DateTimeField(auto_now=True, default=datetime.datetime.now)
    alarm                 = models.BooleanField(default=False)

    def uptime(self):
        now   = datetime.datetime.now()
        delta = now - self.lastest_data.replace(tzinfo=None)
        return delta.seconds


    def status_str(self):
        if self.uptime()>20:
            return 'OFFLINE'
        else:
            return "ONLINE"

    def __unicode__(self):
        return self.identification_number


class Employee(models.Model):
    identification_number = models.CharField(max_length=20)
    first_name            = models.CharField(max_length=20)
    last_name             = models.CharField(max_length=20)
    role                  = models.CharField(max_length=25, null=True)
    department		  = models.IntegerField(choices=DEPARTMENTS, null=True)
    phone                 = models.CharField(max_length=15)
    location_device       = models.OneToOneField(GpsDevice, null=True)
    avatar                = models.ImageField(upload_to='static/profile', blank=True, default='assets/profile/default.png')
     
    def __unicode__(self):
        return self.first_name + " " + self.last_name

    def current_location(self):
        dec_lon = self.location_device.location.get("coordinates")[0]
        dec_lat = self.location_device.location.get("coordinates")[1]
        return self.decimalDegrees2DMS(dec_lon, "Longitude") + ", " + self.decimalDegrees2DMS(dec_lat, "Latitude")

    def decimalDegrees2DMS(self,value,type):
        """
        Converts a Decimal Degree Value into
        Degrees Minute Seconds Notation.
    
        Pass value as double
        type = {Latitude or Longitude} as string
    
        returns a string as D:M:S:Direction
        created by: anothergisblog.blogspot.com 
        """
        degrees = int(value)
        submin = abs( (value - int(value) ) * 60)
        minutes = int(submin)
        subseconds = abs((submin-int(submin)) * 60)
        direction = ""
        if type == "Longitude":
            if degrees < 0:
                direction = "W"
            elif degrees >= 0:
                direction = "E"
            else:
                direction = ""
        elif type == "Latitude":
            if degrees < 0:
                direction = "S"
            elif degrees >= 0:
                direction = "N"
            else:
                direction = "" 
        notation = str(degrees) + u"\u00B0 " + str(minutes) + "' " +\
                   str(subseconds)[0:5] + '" ' + direction
        return notation


class SafetyManager(models.Model):
    user     = models.OneToOneField(User)
    employee = models.ForeignKey(Employee, null=True)

    def __unicode__(self):
        return self.user.username


class Alert(models.Model):
    device         = models.ForeignKey(GpsDevice)
    alert_date     = models.DateTimeField()
    acknowledged   = models.BooleanField(default=False)

    def __unicode__(self):
        return self.device.identification_number


