from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class CustomLoginModel(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

class TourDestination(models.Model):
    img = models.ImageField(upload_to='swipper')
    title = models.CharField(max_length=100)
    price = models.IntegerField(default=0)

class NewTourDestination(models.Model):
    img = models.ImageField(upload_to='swipper')
    title = models.CharField(max_length=100)
    price = models.IntegerField(default=0)

class BookingModel(models.Model):
    full_name = models.CharField(max_length=50, blank=False, null=False)
    email = models.EmailField(max_length=50, blank=False, null=False)
    phone = models.DecimalField(max_digits=12, decimal_places=5, blank=False, null=False)
    visit_date = models.DateField(auto_now=False, blank=False, null=False)
    num_of_pass = models.IntegerField(default=1)
    query = models.TextField()

