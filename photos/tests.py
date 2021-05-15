from django.test import TestCase
from .models import Location, Category, Photos, User

class LocationModelTest(TestCase):
    def setUp(self):
        self.new_location = Location(name="Seoul")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_location, Location))

class CategoryModelTest(TestCase):
    def setUp(self):
        self.new_category = Category(name="art")
    
    def test_instance(self):
        self.assertTrue(isinstance(self.new_category, Category))


class PhotosModelTest(TestCase):
    def setUp(self):
        location = Location(name="Kenya")
        owner = User(username='picasso')

        self.new_pic = Photos(caption="christmas fun", location=location, owner=owner)
    
    def test_instance(self):
        self.assertTrue(isinstance(self.new_pic, Photos))

