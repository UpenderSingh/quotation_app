from django.contrib import admin
from django.urls import path
from user_account.views import (
    UserRegistrationView, UserLoginView, 
    UserProfileView, LoginPageView, CustomerSearchView)
urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('loginpage/', LoginPageView.as_view(), name='loginpage'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('customerpage/', CustomerSearchView.as_view(), name='customerpage'),
]
