from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

greetings_data = {}

def index(request):
    if request.method == "POST":
        name = request.POST.get("name")
        if name:
            greetings_data[name] = greetings_data.get(name, 0) + 1
            return HttpResponseRedirect(reverse("stats", args=[name]))

    return render(request, "greetings/index.html", {
        "total_greetings": sum(greetings_data.values()),
        "users": greetings_data.keys(),
    })

def stats(request, name):
    count = greetings_data.get(name, 0)
    return render(request, "greetings/stats.html", {"name": name, "count": count})