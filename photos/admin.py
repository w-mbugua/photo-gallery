from django.contrib import admin
from .models import Location, Category, Photos

class PhotosAdmin(admin.ModelAdmin):
    filter_horizontal = ('category',)

admin.site.register(Location)
admin.site.register(Category)
admin.site.register(Photos, PhotosAdmin)
