from django.db import models

# 1. PortfolioItem (name, category, image, description)
# 2. Post (title, image, body)
# 3. Contact (name, phone_number, message)
# Create your models here.


class PortfolioItem(models.Model):
    name = models.CharField(max_length=200)
    category = models.TextField(blank=True, null=True)
    image = models.ImageField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)


class Post(models.Model):
    title = models.CharField(max_length=400)
    image = models.ImageField(blank=True, null=True)
    body = models.TextField(blank=True, null=True)

    def __str__(self) -> str:
        return self.title


class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=500)
    message = models.CharField(max_length=400, blank=True, null=True)


class Mycontact(models.Model):
    email = models.CharField(max_length=500, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    phone_name = models.CharField(max_length=360, null=True, blank=True)
