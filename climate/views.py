from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Contact

# Create your views here.
def index(request):
    return render(request, "climate/index.html")

def opinion(request):
    if request.method=="POST":
        contact=Contact()
        name=request.POST.get('name')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        contact.name=name
        contact.email=email
        contact.subject=subject
        contact.save()
        return HttpResponse("<h1> THANKS FOR YOUR OPINION </h1>")

    return render(request, "climate/opinion.html")

def poll(request):
    return render(request, "climate/poll.html")