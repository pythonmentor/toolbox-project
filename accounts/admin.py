
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser

    list_display = (
    'id',
    'email',
    'username',
    'first_name', 
    'last_name',
    'date_of_birth',
    'street_number',
    'street',
    'zipcode',
    'town',
    'mobile',
    'password',
    )      

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('date_of_birth', 'username', 'first_name', 'last_name', 'street_number', 'street', 'zipcode', 'town', 'mobile')}),
    )