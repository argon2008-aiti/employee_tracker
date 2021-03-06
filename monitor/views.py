from django.shortcuts import render, render_to_response, redirect, RequestContext
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django_ajax.decorators import ajax
import django.contrib.auth as auth
from models import *
import datetime


@login_required
def monitor(request):
    now      = datetime.datetime.now()
    username = request.user.get_full_name()

    employees = Employee.objects.all()

    employees_even = [ employee for employee in employees if employee.id%2==0 ]

    employees_odd =  [ employee for employee in employees if employee.id%2!=0 ]

    return render_to_response('base.html', locals())

def mobile(request):
    if request.method == 'POST':
        key   = request.POST.get('key', '')
        lon   = request.POST.get('lon', '')
        lat   = request.POST.get('lat', '')
        alarm = request.POST.get('alarm', '')
        print request.POST 

        # look for device which sent request
        target_device = GpsDevice.objects.get(identification_number=key) 
        target_device.location = {'type':'Point', 'coordinates': [float(lon), float(lat)]}
        
        # condition the alarm variable
        if(alarm=="true"):
            alarm = True
        else:
            alarm = False
        target_device.alarm    = alarm
        target_device.save()
    else:
        return
    
# ajax request 
@ajax
def fetch(request):
    devices = GpsDevice.objects.all()
    entries = []
    for device in devices:
        entries.append(dict({'pk': device.pk, 'coordinates': device.location['coordinates'], \
                'status': device.status_str(), 'employee': device.employee.pk, 'alarm': device.alarm}))
    return entries 

@ajax
def query(request):
    employees = Employee.objects.all()
    entries = []
    for employee in employees:
        entries.append(dict({'name': employee.first_name + " "+ employee.last_name, \
                'department': employee.get_department_display(), 'avatar': employee.avatar.url, 'pk': employee.pk}))
    print entries
    return entries
     

# to log in a user
def login(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')

    user     = auth.authenticate(username=username, password=password)
    
    if user is not None:
        if user.is_active:
            auth.login(request, user)
            if request.POST.has_key('next'):
                return redirect(request.POST['next']) 
            return redirect('/monitor') 

        else:
            pass # user is valid but not active

    else:
        return render_to_response('login.html', {'status': username},
                context_instance=RequestContext(request))


# to log out a user
def logout(request):
    request.user.logout()

