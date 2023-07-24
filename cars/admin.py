from django.contrib import admin
from .models import Car
from django.utils.html import format_html




class CarAdmin(admin.ModelAdmin):
    
    def thumbnail(self,object):
        return format_html('<img src="{}"  width="40" style="border-radius=50px;" />'.format(object.car_photo.url))
    
    thumbnail.short_description='Car Image'
    
    list_display=('car_title','color','model','year','body_style','fuel_type','is_featured')
    list_display_links=('id','thumbnail')

# Register your models here.
admin.site.register(Car)   