from django.db import models

# Create your models here.
class MainModel(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    author = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    created_at = models.DateField(auto_now_add=True)