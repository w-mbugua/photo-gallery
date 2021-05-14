from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
class Location(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Photos(models.Model):
    caption = models.CharField(max_length=200)
    date_posted = models.DateTimeField(auto_now_add=True)
    location = models.ForeignKey(Location, models.SET_NULL, blank=True, null=True)
    category = models.ManyToManyField(Category)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    image = CloudinaryField('image')

    class Meta:
        ordering = ['date_posted']

    def __str__(self):
        return self.caption

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    def update_image(self):
        pass

    @classmethod
    def get_image_by_id(cls, id):
        image = cls(pk=id)
        return image

    @classmethod
    def filter_by_location(cls, location):
        image = cls(location=location)
        return image

    @classmethod
    def search_by_category(cls, category):
        image = cls(category=category)
        return image





