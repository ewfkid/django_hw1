from django.shortcuts import render

from django.http import HttpResponse
from .models import Greeting
from django.utils.timezone import now

def hello(request, name):
    Greeting.objects.create(name=name, timestamp=now())
    return HttpResponse(f"Hello, {name}!")


def stats(request):
    total_greetings = Greeting.objects.count()
    return HttpResponse(f"Total greetings: {total_greetings}")

def user_stats(request, name):
    greetings = Greeting.objects.filter(name=name).order_by('-timestamp')

    if not greetings.exists():
        return HttpResponse(f"No greetings found for {name}")

    response_text = f"Greetings for {name}:<br>"
    for greeting in greetings:
        response_text += f"{greeting.timestamp}<br>"

    return HttpResponse(response_text)
