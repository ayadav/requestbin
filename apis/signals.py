import django.dispatch

git_hook_received = django.dispatch.Signal(providing_args=["payload"])
