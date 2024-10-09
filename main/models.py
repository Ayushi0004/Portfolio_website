from django.db import models

# Create your models here.

class Project(models.Model):
    image=models.ImageField(blank=True)
    title=models.CharField(max_length=50, blank=True)
    link = models.URLField(blank=True, null=True)
    description=models.CharField(max_length=150, blank=True)

    
class Skill(models.Model):
    name=models.CharField(max_length=25, blank=True)
    percent=models.IntegerField(max_length=2, blank=True)
    des=(models.CharField(max_length=150, blank=True))

# class Certificate(models.Model):
#     image=models.ImageField(blank=True)
#     title=models.CharField(max_length=50, blank=True)
#     description=models.CharField(max_length=50, blank=True)
