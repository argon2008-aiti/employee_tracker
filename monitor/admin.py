from django.contrib import admin
from monitor.models import *
from leaflet.admin import LeafletGeoAdmin

admin.site.register(GpsDevice, LeafletGeoAdmin)
admin.site.register(Employee)
admin.site.register(SafetyManager)
admin.site.register(Alert)
