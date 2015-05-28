from rest_framework import serializers
from monitor.models import GpsDevice

class GpsDeviceSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = GpsDevice
        fields = ('pk', 'location', 'employee')
