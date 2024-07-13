from celery import shared_task
from time import sleep

@shared_task
def send_emai():
    sleep(3)
    print('done sending email')