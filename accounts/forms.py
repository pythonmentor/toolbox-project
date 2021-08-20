from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class CustomUserCreationForm(forms.ModelForm):

    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(
    label='Repeat Password', widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'first_name', 'last_name', 'email','date_of_birth', 'street', 'street_number', 'street', 'zipcode', 'town', 'mobile']
        widgets = {
            "username": forms.TextInput(attrs={
                "class": "registration-username", 
                "placeholder": "Entrez votre nom d'utilisateur"
                }), 
            "first_name": forms.TextInput(attrs={
                "class": "registration-first_name", 
                "placeholder": "Entrez votre prénom"
                }),            
            "last_name": forms.TextInput(attrs={
                "class": "registration-last_name", 
                "placeholder": "Entrez votre nom de famille"
                }),
            "email": forms.EmailInput(attrs={
                "class": "registration-email", 
                "placeholder": "Entrez votre email"
                }),
            "date_of_birth": forms.DateInput(attrs={
                "class": "registration-date_of_birth",
                "type": "date"
                }),
            
        }
    
class CustomUserChangeForm(forms.ModelForm):
   class Meta:
        model = CustomUser
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'date_of_birth', 'street_number', 'street', 'zipcode', 'town', 'mobile']
    