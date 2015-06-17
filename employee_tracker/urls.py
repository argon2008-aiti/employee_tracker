from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()


from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'employee_tracker.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^monitor/', 'monitor.views.monitor', name='monitor'),
    url(r'^login/', 'monitor.views.login', name='login'),
    url(r'^logout/', 'django.contrib.auth.views.logout', {'next_page':'/login/'}),
    url(r'^mobile-request/', 'monitor.views.mobile', name='mobile'),
    url(r'^fetch/', 'monitor.views.fetch', name='fetch'),
    url(r'^query', 'monitor.views.query', name='query'),
)

urlpatterns += staticfiles_urlpatterns()
