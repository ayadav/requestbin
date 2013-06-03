from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from apis.resources import IssueResource

issue_resource = IssueResource()

urlpatterns = patterns('',
       (r'^apis/', include(issue_resource.urls)),

       # Uncomment the next line to enable the admin:
       url(r'^admin/', include(admin.site.urls)),
   )
