from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_hooks.signals import raw_hook_event
from django.contrib.auth.models import User
import datetime
from django.http.response import HttpResponse
# Create your views here.

@csrf_exempt
def webhook(request):
    print request.body
    return HttpResponse()

def event(request):
    user = User.objects.get(username='chetan')
    raw_hook_event.send(
        sender=None,
        event_name='user.signup',
        payload={
            'username': user.username,
            'email': 'chetan@callhub.io',
            'when': datetime.datetime.now().isoformat()
        },
        user=user # required: used to filter Hooks
    )
    return HttpResponse()

