from django.contrib import admin
from django.urls import path
from django.views.generic.base import TemplateView
from django.contrib.auth import views
from tekitcom.forms import UserLoginForm

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", TemplateView.as_view(template_name="home.html"), name="home"),
    path("login/", views.LoginView.as_view(template_name='login.html', authentication_form=UserLoginForm), name="login"),
    path('logout/', views.LogoutView.as_view(template_name='login.html'), name='logout'),
]
