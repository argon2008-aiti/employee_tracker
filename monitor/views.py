from django.shortcuts import render, render_to_response, redirect, RequestContext
from datetime import datetime
from django.contrib.auth.decorators import login_required
import django.contrib.auth as auth

# Create your views here.

@login_required
def monitor(request):
    now      = datetime.now()
    username = request.user.get_full_name()
    return render_to_response('base.html', locals())

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
def log_user_out(request):
    request.user.logout()
