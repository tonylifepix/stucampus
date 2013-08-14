from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'stucampus.master.views.index', name='home'),
    url(r'^lost_and_found/', include('stucampus.lost_and_found.urls',
                                     namespace='lost_and_found') ),
    # Examples:
    # url(r'^$', 'stucampus.views.home', name='home'),
    # url(r'^stucampus/', include('stucampus.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

handler404 = 'stucampus.master.views.page_not_found'
