from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from apis.resources import GitHookResource

git_hook_resource = GitHookResource()

urlpatterns = patterns('',
       (r'^apis/', include(git_hook_resource.urls)),

       # Uncomment the next line to enable the admin:
       url(r'^admin/', include(admin.site.urls)),
   )
