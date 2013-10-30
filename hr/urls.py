from django.conf.urls import patterns, include, url

from django.conf.urls.static import static
import employee 
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
#admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'employee.views.hello', name='home'),
    url(r'^template_test/$', 'employee.views.template_test', name='test'),
    url(r'^form_test/$', 'employee.views.form_test', name='form_test'),
    url(r'employee_list/$', 'employee.views.employee_list', name = 'employee_list')
    # url(r'^$', 'web.views.home', name='home'),
    # url(r'^web/', include('web.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)