from django.urls import path
from .models import*
from .views import*

urlpatterns=[
    path('signup/',signup_page),
    path('',login_page),
    path('logout/',logout_page),
]