
from django.shortcuts import render
from django.utils.timezone import now
from .models import Greeting

def hello(request, name):
    # Создаём запись в базе данных
    Greeting.objects.create(name=name, timestamp=now())
    return render(request, 'greetings/hello.html', {'name': name})

def stats(request):
    total_greetings = Greeting.objects.count()
    return render(request, 'greetings/stats.html', {'total_greetings': total_greetings})

def user_stats(request, name):
    greetings = Greeting.objects.filter(name=name).order_by('-timestamp')
    return render(request, 'greetings/stats_by_name.html', {'name': name, 'greetings': greetings})