from tastypie.resources import ModelResource
from tastypie import fields
from tastypie.authorization import DjangoAuthorization
from django.conf.urls import url
from tastypie import fields, http
import copy

from tracker.models import Issue

class IssueResource(ModelResource):

    class Meta:
        queryset = Issue.objects.all()
        resource_name = 'issues'
        authorization = DjangoAuthorization()


    def prepend_urls(self):
        """
        The standard URLs this ``Resource`` should respond to.
        """
        return [
            url(r"^(?P<resource_name>{0})/(?P<{1}>\d+).json$" .format(self._meta.resource_name, self._meta.detail_uri_name),
                self.wrap_view('issue_update'), name="issue_update"),
        ]

    def issue_update(self, request, **kwargs):
        response = self.create_response(request, dict(
            request=[copy.copy(request).__dict__]
        ), response_class=http.HttpAccepted)

        return response