from django.shortcuts import render
from django.http import HttpResponse ,JsonResponse
import time
import requests

from .tasks import send_emai
# Create your views here.

def send_email(request):
    send_emai.delay()
    return HttpResponse("<h1>Email sent successfully</h1>")

def test(request):
    response  = requests.get('https://56265dcd-4ee7-4c3b-b7d4-bc84d1bbe1b5.mock.pstmn.io/test/delay/5')
    return JsonResponse(response.json())