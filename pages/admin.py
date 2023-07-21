from django.contrib import admin
from .models import Teams
from django.utils.html import format_html

# Register your models here.
class TeamAdmin(admin.ModelAdmin):
    def thumbnail(self,object):
        return format_html('<img src="{}"  width="40" style="border-radius=50px;" />'.format(object.photo.url))
    
    thumbnail.short_description='Photo'
        
    list_display=('id','thumbnail','firstname','designation','created_date')
    list_display_links=('firstname','designation','created_date')
    search_fields=('firstname','lastname','designation')
     
    
    
admin.site.register(Teams,TeamAdmin) 