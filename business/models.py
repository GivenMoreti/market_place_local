from django.db import models
from django.contrib.auth.models import User

class Business(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    email = models.EmailField(unique=True)
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)
    website_url = models.URLField(blank=True, null=True)
    logo = models.ImageField(upload_to='business_logos', blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.name
