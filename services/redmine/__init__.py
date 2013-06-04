from django.dispatch import receiver
from apis.signals import git_hook_received
import re
import traceback
import requests
from django.conf import settings
from django.template.loader import render_to_string
import json


@receiver(git_hook_received)
def handle_payload(sender, **kwargs):
    try:
        payload = kwargs.get('payload', [])

        if payload:
            redmine_server = getattr(settings, 'REDMINE_SETTINGS', {})
            api_url = redmine_server['REDMINE_ISSUE_API_URI']
            api_key = redmine_server['X_Redmine_API_Key']
            verify_ssl = redmine_server['VERIFY_SSL']

            for commit in payload.get('commits', []):
                msg = commit.get('message', '')
                matches  = re.findall(r'#(\d+)', msg)
                if matches:
                    payload = {'issue' : {}}
                    payload['issue']['notes'] = render_to_string('redmine/commit_msg_template.html', {'commit': commit})
                    for issue_id in matches:
                        url = api_url%({'id':issue_id})
                        headers = {'content-type': 'application/json', 'X-Redmine-API-Key' : api_key}
                        requests.put(url, data = json.dumps(payload), headers = headers, verify = verify_ssl)

    except:
        print traceback.format_exc()