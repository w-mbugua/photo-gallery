from django.shortcuts import render
from .models import Photos

def home(request):
    images = Photos.objects.all()
    return render(request, 'photos/home.html', {"images": images})
