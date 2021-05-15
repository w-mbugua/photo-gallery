from django.test import TestCase
from .models import Location, Category, Photos, User

class LocationModelTest(TestCase):
    def setUp(self):
        self.new_location = Location(name="Seoul", id=15)
        self.new_location2 = Location(name="Nairobi")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_location, Location))
    
    def test_save_method(self):
        self.new_location.save_loc()
        locations = Location.objects.all()
        print(len(locations))
        self.assertTrue(len(locations) > 0)
    
    def test_delete_method(self):
        self.new_location.delete_loc()
        self.assertTrue(self.new_location.DoesNotExist)

class CategoryModelTest(TestCase):
    def setUp(self):
        self.new_category = Category(name="art", id=15)
    
    def test_instance(self):
        self.assertTrue(isinstance(self.new_category, Category))
    
    def test_save_method(self):
        self.new_category.save_cat()
        categories = Category.objects.all()
        print(len(categories))
        self.assertTrue(len(categories) > 0)
    
    def test_delete_method(self):
        self.new_category.delete_cat()
        self.assertTrue(self.new_category.DoesNotExist)


class PhotosModelTest(TestCase):
    def setUp(self):
        self.location = Location(name="Kenya")
        self.location.save_loc()
        self.owner = User(username='picasso')
        self.owner.save()

        self.new_pic = Photos(id=15, caption="christmas fun", location=self.location, owner=self.owner)
    
    def test_instance(self):
        self.assertTrue(isinstance(self.new_pic, Photos))
    
    def test_save_method(self):
        self.new_pic.save_image()
        images = Photos.objects.all()
        print(len(images))
        self.assertTrue(len(images) > 0)
    
    def test_delete_method(self):
        self.new_pic.delete_image()
        self.assertTrue(self.new_pic.DoesNotExist)

