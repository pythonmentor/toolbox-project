from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings

def fooview(request):
    
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        message=request.POST.get('message')
        send_mail(subject= subject,message= message,from_email=settings.DEFAULT_FROM_EMAIL,recipient_list = [email],fail_silently  = True,)
        
        return redirect('fooview')

    return render(request,'baar.html',{})