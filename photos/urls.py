from django.urls import path
from .views import home, image_search
urlpatterns = [
    path('', home, name='home'),
    path('search/', image_search, name="image_search")
]