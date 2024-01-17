from django.db import models
from tinymce.models import HTMLField

class Services2(models.Model):
    heading = models.CharField(max_length=200)
    description = HTMLField()
    image = models.ImageField(upload_to='off_img/')


class Register1(models.Model):
    address=models.CharField(max_length=111)
    email=models.EmailField(max_length=111)
    birth=models.CharField(max_length=33)
    registerdate=models.CharField(max_length=44)
    registertime=models.CharField(max_length=41)
    phone=models.CharField(max_length=11)

class Newmodel(models.Model):
    name=models.CharField( max_length=50)
    email=models.EmailField( max_length=254)
    phone=models.CharField( max_length=50)
