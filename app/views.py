from django.shortcuts import render
from app.models import *
# Create your views here.

def display_topics(request):
    QSTO=Topic.objects.all()
    d={'QSTO':QSTO}
    return render(request,'display_topics.html',d)


def display_webpages(request):
    QSWO=Webpage.objects.all()
    d={'QSWO':QSWO}
    return render(request,'display_webpages.html',d)

def display_accessrecord(request):
    QSARO=Accessrecords.objects.all()
    d={'QSARO':QSARO}
    return render(request,'display_accessrecord.html',d)