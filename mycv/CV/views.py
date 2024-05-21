from django.shortcuts import render
from .models import Profile

# Create your views here.

def front(req):
    data = Profile.objects.all()
    return render(req, "profile.html", {"data": data}) 
