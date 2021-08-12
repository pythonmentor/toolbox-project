from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class CustomUser(AbstractUser):
    date_of_birth = models.DateField("date_of_birth", blank=True, null=True)
    address = models.TextField("address", blank=True, null=True)
    mobile = PhoneNumberField("mobile", blank=True, null=True)

    class Meta:
        ordering = ['last_name']
    
    def __str__(self):
        return f"{self.username}: {self.first_name} {self.last_name} {self.date_of_birth} {self.address} {self.mobile}"