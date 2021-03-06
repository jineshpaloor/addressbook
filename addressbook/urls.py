from django.conf.urls import patterns, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('addressbook.views',
    # Examples:
    url(r'^$', 'home', name='home'),
    url(r'^address/add/$', 'add_address', name='add-address'),
    url(r'^address/all/$', 'all_address', name='all-address'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
