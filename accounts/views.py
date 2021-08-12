from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from .forms import CustomUserCreationForm


def register(request):
    if request.user.is_authenticated:
        return redirect('pages:home')

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = CustomUserCreationForm()

    context = {
        'form' : form,
    }
            
    return render(request, 'accounts/register.html', context)

def profil(request):

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = CustomUserCreationForm()

    context = {
        'form' : form,
    }
            
    return render(request, 'accounts/profil.html', context)
