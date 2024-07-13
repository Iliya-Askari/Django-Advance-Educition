from django.shortcuts import render
from django.http import HttpResponse
import time

from .tasks import send_emai
# Create your views here.

def send_email(request):
    send_emai.delay()
    return HttpResponse("<h1>Email sent successfully</h1>")