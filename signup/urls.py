from django.urls import path
from .models import*
from .views import*

urlpatterns=[
    path("signup/",signup_page),
    path("login/",login_page)
]