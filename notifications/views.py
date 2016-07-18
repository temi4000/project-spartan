import json

from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseForbidden, HttpResponse

from .models import Notification


@csrf_exempt
def seen(request):
    if request.method == "POST":
        if request.POST.get('notif'):
            notif_id = request.POST.get("notif")
            notification = Notification.objects.get(id_hash=notif_id)
            if notification.seen:
                return HttpResponseForbidden()
            notification.seen = True
            notification.save()
            context = {"result": "success",
                       "type": notification.not_type}
            return HttpResponse(json.dumps(context),
                                content_type='application/json')
    return HttpResponseForbidden()


@csrf_exempt
def notification_delete(request):
    if request.method == "POST":
        if request.POST.get("id"):
            notif_id = request.POST.get("id")
            notification = Notification.objects.get(id_hash=notif_id)
            notification.delete()
            return HttpResponse(json.dumps({'result': 'succes'}),
                                content_type='application/json')
    return HttpResponseForbidden()