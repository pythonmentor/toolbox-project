from django.urls import path, include

from .views import HomePageView, ContactPageView

app_name = 'pages'

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('contact/', ContactPageView.as_view(), name='contact'),
    path('accounts/', include('accounts.urls')),
]