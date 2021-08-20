from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext as _
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class CustomUser(AbstractUser):
    date_of_birth = models.DateField(_("date of birth"), blank=True, null=True)
    street_number=models.IntegerField(_("street number"), blank=True, null=True)
    street = models.CharField(_("street"), max_length=500, blank=True, null=True)
    zipcode = models.IntegerField(_("zip code"), blank=True, null=True)
    town = models.CharField(_("town"), max_length=200, blank=True, null=True)
    mobile = PhoneNumberField(_("mobile"), blank=True, null=True)

    class Meta:
        ordering = ['last_name']
    
    def __str__(self):
        return f"{self.username}: {self.first_name} {self.last_name} {self.date_of_birth} {self.street_number} {self.street} {self.zipcode} {self.town} {self.mobile}"
