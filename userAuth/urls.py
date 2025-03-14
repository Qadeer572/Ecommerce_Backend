from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from . import views
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('login', views.login_view, name='login_view'),
    path('signup', views.register_view, name='signup_view'),
    
]