from django.db import models

# Create your models here.

class CreateMenuItem(models.Model):
    name = models.CharField(max_length=300)
    img =  models.ImageField(upload_to="pics")