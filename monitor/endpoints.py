from ajax.exceptions import AJAXError
import json
import ajax
from monitor.models import GpsDevice, Employee
from monitor.json_serializer import JSONSerializer
from ajax.decorators import allowed_methods
import django.contrib.auth as auth

class EmployeeEndpoint(ajax.endpoints.ModelEndpoint):
    
    @allowed_methods('get', 'list')
    def authenticate(self, request, application, method):
        if request.user is not None:
            print "called"
            if request.user.is_authenticated():
                print "called again"
                return True
        else:
            return False
        

ajax.endpoint.register(Employee, EmployeeEndpoint)


def right_back(request):
    gps  = GpsDevice.objects.all()
    jsonSerializer = JSONSerializer()
    return {'gps': jsonSerializer.serialize(gps)}
