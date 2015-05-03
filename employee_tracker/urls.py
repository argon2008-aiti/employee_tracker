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
)

urlpatterns += staticfiles_urlpatterns()
