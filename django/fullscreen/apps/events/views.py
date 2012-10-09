import datetime
from django.shortcuts import render
from models import Event

def home(request):
    now = datetime.datetime.now()
    today = datetime.date.today()
    try:
        am_event = Event.objects.filter(when__gte=today, category='am').order_by('when')[0]
    except IndexError:
        am_event = None
    
    try:
        pm_event = Event.objects.filter(when__gte=now, category='pm').order_by('when')[0]
    except IndexError:
        pm_event = None
    
    return render(request, 'base.html', locals())