import json

from django.shortcuts import render
from django.views import View


class WebhookReceiveView(View):
    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        pass
