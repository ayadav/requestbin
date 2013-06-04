from tastypie.resources import Resource
from django.conf.urls import url
from tastypie import http
from apis.signals import git_hook_received
import json
from django.conf import settings

class GitHookResource(Resource):

    class Meta:
        resource_name = 'git_hooks'
        secret_key = settings.GIT_WEBHOOK_SECRET

    def prepend_urls(self):
        """
        The standard URLs this ``Resource`` should respond to.
        """
        return [
            url(r"^(?P<resource_name>{0})/(?P<secret_key>{1})/$" .format(self._meta.resource_name, self._meta.secret_key),
                self.wrap_view('handle_hook'), name="handle_hook"),
        ]

    def handle_hook(self, request, **kwargs):
        payload = json.loads(request.REQUEST['payload'])

        git_hook_received.send(sender=self, payload=payload)

        response = self.create_response(request, dict(
            request=[]
        ), response_class=http.HttpAccepted)

        return response