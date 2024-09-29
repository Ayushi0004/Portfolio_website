from django.db import models

class HomeContent(models.Model):
    title = models.CharField(max_length=200, default="Welcome to My Portfolio")
    description = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.title

class About(models.Model):
    title = models.CharField(max_length=100, default="About Me")
    description = models.TextField()
    profile_image = models.ImageField(upload_to='about/', blank=True, null=True)
    
    def __str__(self):
        return self.title

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    link = models.URLField(blank=True, null=True)
    date = models.DateField()

    def __str__(self):
        return self.title

class Skill(models.Model):
    name = models.CharField(max_length=100)
    proficiency = models.IntegerField(help_text="Enter proficiency level from 1 to 10")
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Contact(models.Model):
    email = models.EmailField()
    phone = models.CharField(max_length=15, blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    github = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.email

class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    link = models.CharField(max_length=100)

    def __str__(self):
        return self.name