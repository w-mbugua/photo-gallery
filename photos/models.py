from django.db import models
from django.contrib.auth.models import User

class Location(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Photos(models.Model):
    caption = models.CharField(max_length=50)
    date_posted = models.DateTimeField(auto_now_add=True)
    Location = models.ForeignKey(Location, models.SET_NULL, blank=True, null=True)
    category = models.ManyToManyField(Category)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.caption



