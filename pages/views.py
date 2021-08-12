from django.views.generic import TemplateView
from django.http import HttpResponse
from datetime import datetime


class HomePageView(TemplateView):
    template_name = 'pages/home.html'
   
    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['myDate'] = datetime.now()
        return context


class ContactPageView(TemplateView):
    template_name = 'pages/contact.html'
        