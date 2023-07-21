from django.db import models

# Create your models here.
class Teams(models.Model):
    firstname= models.CharField(max_length=255)
    lastname= models.CharField(max_length=255)
    photo=models.ImageField(upload_to='photos/%Y/%M/%D/')
    designation= models.CharField(max_length=255)
    facebook_link=models.URLField(max_length=100)
    google_plus_link= models.URLField(max_length=100)
    created_date= models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.firstname
    