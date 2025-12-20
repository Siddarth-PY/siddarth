from django.urls import path
from .views import*
urlpatterns=[
       path("form/",formpage),
       path("display/",display),
       path("display/<int:emp_1>/",update_page,name="update_emp"),
       path("delete/<int:emp_2>/",delete_page,name="delete_emp"),   


]