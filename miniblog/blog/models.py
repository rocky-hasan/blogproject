from django.db import models


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=150)
    desc = models.TextField()


class Contact(models.Model):
    username = models.CharField(max_length=70)
    email = models.EmailField(max_length=100)
    address = models.CharField(max_length=200)
    message = models.TextField()
