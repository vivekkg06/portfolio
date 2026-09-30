from django.db import models

# Create your models here.



class Profile(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=150)
    about = models.TextField()
    profile_image = models.ImageField(upload_to="profile/", blank=True, null=True)

    def __str__(self):
        return self.name


class Service(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    icon = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.title


class Skill(models.Model):
    name = models.CharField(max_length=100)
    percentage = models.PositiveIntegerField(default=80)

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    image = models.ImageField(upload_to="projects/", blank=True, null=True)
    github_url = models.URLField(blank=True)
    live_url = models.URLField(blank=True)

    def __str__(self):
        return self.title


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name