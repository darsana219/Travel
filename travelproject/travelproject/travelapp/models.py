from django.db import models

# Create your models here.
class Place(models.Model):
    name = models.CharField(max_length = 250)
    img = models.ImageField(upload_to = 'pics')
    desc = models.TextField()

class People(models.Model):
    p_name = models.CharField(max_length = 250)
    p_img = models.ImageField(upload_to = 'ppics')
    p_desc = models.TextField()

# to know the name of field in place table
# def __str__(self):
#     return self.name