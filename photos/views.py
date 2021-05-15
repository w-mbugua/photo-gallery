from django.shortcuts import render
from .models import Photos
# from  django.http import HttpResponse


def home(request):
    images = Photos.objects.all().order_by('-id')
    return render(request, 'photos/home.html', {"images": images})

def image_search(request):
    keyword = request.GET.get('photo')
    images = Photos.search_by_term(keyword)
    message = f"{keyword}".capitalize()
    return render(request, 'photos/search.html', {"message": message, "images": images})





