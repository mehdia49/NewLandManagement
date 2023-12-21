from django.db import models
from django.contrib.auth.models import User 

class PhoneNumber(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)  # You can adjust the max length as needed

    def __str__(self):
        return self.phone_number
