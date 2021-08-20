from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'accounts'

urlpatterns = [
    path('register/', views.register, name = 'register'),
    path('profil/', views.profil, name='profil'),
    path('modifprofil/<id>', views.modifprofil, name = 'modifprofil'),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html', redirect_authenticated_user = True), name = 'login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='accounts/logout.html', next_page='pages:home'), name = 'logout'),
]

